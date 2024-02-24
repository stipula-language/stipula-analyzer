'''
visitoroutput.py
'''
from datetime import timedelta
import functools
import json

from classes.data.functionvisitorentry import FunctionVisitorEntry
from classes.data.eventvisitorentry import EventVisitorEntry
from classes.data.valuedependency import ValueDependency



NOW = 'now'



class VisitorOutput:



    def __init__(self):
        self.field_id_map = {}
        self.Q0 = None
        self.C = set()
        self.Gamma = {}
        self.dependency_t_map = {}
        self.t = {}
        self.R = {}
        self.reachability_constraint = set()
        self.warning_code = set()
        self.expired_code = {}
        self.unreachable_code = set()



    def __str__(self):
        return json.dumps({
            'field_id_map': {field_id: str(value) for field_id, value in self.field_id_map.items()},
            'Q0': self.Q0,
            'C': [str(visitor_entry) for visitor_entry in self.C],
            'Gamma': {str(event_visitor_entry): str(function_visitor_entry) for event_visitor_entry, function_visitor_entry in self.Gamma.items()},
            'dependency_t_map': {str(visitor_entry): list(field_id_tuple) for visitor_entry, field_id_tuple in self.dependency_t_map.items()},
            't': {str(visitor_entry): str(time_delta) for visitor_entry, time_delta in self.t.items()},
            'R': {str(visitor_entry): [[str(visitor_entry) for visitor_entry in visitor_entry_tuple] for visitor_entry_tuple in visitor_entry_tuple_set] for visitor_entry, visitor_entry_tuple_set in self.R.items()},
            'reachability_constraint': [[[str(dependency) for dependency in dependency_tuple_1], [str(dependency) for dependency in dependency_tuple_2]] for dependency_tuple_1, dependency_tuple_2 in self.reachability_constraint],
            'warning_code': [[str(visitor_entry_1), str(visitor_entry_2)] for visitor_entry_1, visitor_entry_2 in self.warning_code],
            'expired_code': {str(visitor_entry): str(time_delta) for visitor_entry, time_delta in self.expired_code.items()},
            'unreachable_code': [str(visitor_entry) for visitor_entry in self.unreachable_code]
        }, indent=2)
    


    def set_field_id_value(self, field_id, value):
        self.field_id_map[field_id] = value



    def set_init_state_id(self, state_id):
        self.Q0 = state_id



    def add_visitor_entry(self, visitor_entry):
        self.C.add(visitor_entry)



    def set_event_definition(self, event_visitor_entry, function_visitor_entry):
        self.Gamma[event_visitor_entry] = function_visitor_entry



    def set_dependency_t(self, event_visitor_entry, field_id_tuple):
        self.dependency_t_map[event_visitor_entry] = field_id_tuple



    def set_t(self, event_visitor_entry, time_delta):
        self.t[event_visitor_entry] = time_delta



    def is_cyclic(self, function_visitor_entry):
        return function_visitor_entry.start_state in {visitor_entry.end_state for visitor_entry in functools.reduce(lambda a, b: a.union(set(b)), self.R[function_visitor_entry], set())}



    # TODO DSE questa funzione potrebbe essere migliorata, per gli eventi bisogna anche considerare il costrutto now, perché altrimenti l'evento ha una data fissa
    def Theta(self, visitor_entry_tuple):
        # Questo valore funge da accumulatore
        value_dependency = ValueDependency(timedelta(seconds=0), ())
        # Controllo tutte le funzioni
        for function_visitor_entry in (visitor_entry for visitor_entry in visitor_entry_tuple if isinstance(visitor_entry, FunctionVisitorEntry)):
            # Aggiungo il simbolo della funzione
            value_dependency.dependency_tuple = tuple(sorted([
                *value_dependency.dependency_tuple,
                f"{function_visitor_entry.start_state}:{function_visitor_entry.handler}.{function_visitor_entry.code_id}:{function_visitor_entry.end_state}"
            ]))
            # Controllo tutti gli eventi definiti dalla funzione presenti nella tupla
            for event_visitor_entry in (event_visitor_entry for event_visitor_entry, function_event_visitor_entry in self.Gamma.items() if function_event_visitor_entry == function_visitor_entry and event_visitor_entry in visitor_entry_tuple):
                # Aggiungo la time expression dell'evento
                value_dependency.value += self.t[event_visitor_entry] + functools.reduce(lambda a, b: a + b, (self.field_id_map[field_id] for field_id in self.dependency_t_map[event_visitor_entry] if field_id != NOW and self.field_id_map[field_id] is not None), timedelta(seconds=0))
                value_dependency.dependency_tuple = tuple(sorted([
                    *value_dependency.dependency_tuple,
                    *(field_id for field_id in self.dependency_t_map[event_visitor_entry] if field_id != NOW and self.field_id_map[field_id] is None)
                ]))
        return value_dependency



    def T(self, visitor_entry_tuple_set):
        return {self.Theta(visitor_entry_tuple) for visitor_entry_tuple in visitor_entry_tuple_set}



    def is_solvable(self, previous_value_dependency, value_dependency):
        min_value = min(previous_value_dependency.value, value_dependency.value)
        previous_value = previous_value_dependency.value - min_value
        value = value_dependency.value - min_value
        previous_field_id_list = list(previous_value_dependency.dependency_tuple)
        field_id_list = list(value_dependency.dependency_tuple)
        index = 0
        while index < len(previous_field_id_list):
            if previous_field_id_list[index] in field_id_list:
                field_id_list.remove(previous_field_id_list[index])
                previous_field_id_list.pop(index)
                continue
            index += 1
        if not field_id_list and previous_value > value:
            return False
        return True



    def compute_R(self):
        is_step_0 = True
        is_loop = is_step_0
        while is_loop:
            is_loop = is_step_0
            # Prima regola: precalcolo il valore iniziale
            self.R = {visitor_entry: ({
                (
                    visitor_entry,
                )
            } if isinstance(visitor_entry, FunctionVisitorEntry) and visitor_entry.start_state == self.Q0 else set()) for visitor_entry in self.C}
            is_change = True
            while is_change:
                is_change = False
                for visitor_entry in self.C:
                    add_visitor_entry_tuple_set = set()
                    match type(visitor_entry).__name__:
                        # Seconda regola: calcolo per le funioni
                        case FunctionVisitorEntry.__name__:
                            for previous_visitor_entry in (previous_visitor_entry for previous_visitor_entry in self.C if previous_visitor_entry.end_state == visitor_entry.start_state):
                                add_visitor_entry_tuple_set.update({(
                                    *visitor_entry_tuple,
                                    *((
                                        visitor_entry,
                                    ) if visitor_entry not in visitor_entry_tuple else ())
                                ) for visitor_entry_tuple in self.R[previous_visitor_entry]})
                        # Terza regola: calcolo per gli eventi
                        case EventVisitorEntry.__name__:
                            for previous_visitor_entry in (previous_visitor_entry for previous_visitor_entry in self.C if previous_visitor_entry.end_state == visitor_entry.start_state):
                                for previous_visitor_entry_tuple in (previous_visitor_entry_tuple for previous_visitor_entry_tuple in self.R[previous_visitor_entry] if self.Gamma[visitor_entry] in previous_visitor_entry_tuple):
                                    # Funzione che definisce non ciclica, calcolo anche i tempi
                                    for previous_value_dependency in self.T({
                                        previous_visitor_entry_tuple
                                    }):
                                        for value_dependency in self.T({(
                                            *visitor_entry_tuple,
                                            *((
                                                visitor_entry,
                                            ) if visitor_entry not in visitor_entry_tuple else ())
                                        ) for visitor_entry_tuple in self.R[self.Gamma[visitor_entry]]}):
                                            if (not self.is_cyclic(self.Gamma[visitor_entry]) and not self.is_solvable(previous_value_dependency, value_dependency)) and not is_step_0:
                                                continue
                                            add_visitor_entry_tuple_set.add((
                                                *previous_visitor_entry_tuple,
                                                *((
                                                    visitor_entry,
                                                ) if visitor_entry not in previous_visitor_entry_tuple else ()),
                                            ))
                    is_change = is_change or bool(add_visitor_entry_tuple_set.difference(self.R[visitor_entry]))
                    self.R[visitor_entry].update(add_visitor_entry_tuple_set)
            is_step_0 = False



    def compute_reachability_constraint(self):
        # TODO DSE da implementare
        pass



    def compute_warning_code(self):
        # TODO DSE da implementare
        pass



    def compute_expired_code(self):
        # Identifico gli eventi già scaduti
        remove_event_visitor_entry_set = set()
        for event_visitor_entry in (visitor_entry for visitor_entry in self.C if isinstance(visitor_entry, EventVisitorEntry)):
            is_executable = False
            value = self.t[event_visitor_entry]
            for field_id in self.dependency_t_map[event_visitor_entry]:
                if field_id == NOW:
                    is_executable = True
                    break
                if self.field_id_map[field_id] is None:
                    is_executable = True
                    break
                value += self.field_id_map[field_id]
            if is_executable:
                continue
            if value < timedelta(seconds=0):
                remove_event_visitor_entry_set.add(event_visitor_entry)
                self.expired_code[event_visitor_entry] = value
        self.C = self.C.difference(remove_event_visitor_entry_set)



    # TODO DSE si potrebbe riscrivere un po' meglio
    def compute_unreachable_code(self):
        # Calcolo l'unreachable-code
        reachable_visitor_entry_set = set()
        for visitor_entry_tuple_set in self.R.values():
            for visitor_entry_tuple in visitor_entry_tuple_set:
                for visitor_entry in visitor_entry_tuple:
                    reachable_visitor_entry_set.add(visitor_entry)
        self.unreachable_code = self.C.difference(reachable_visitor_entry_set)
