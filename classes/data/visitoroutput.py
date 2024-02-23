'''
visitoroutput.py
'''
from datetime import timedelta
import functools
import json

from classes.exceptions.loopexception import LoopException
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
        self.RC = {}
        self.T = {}
        self.R = set()
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
            'RC': {str(visitor_entry): [[str(visitor_entry) for visitor_entry in visitor_entry_tuple] for visitor_entry_tuple in visitor_entry_tuple_set] for visitor_entry, visitor_entry_tuple_set in self.RC.items()},
            'T': {str(visitor_entry): [{
                'value': str(value_dependency.value),
                'dependency_tuple': list(value_dependency.dependency_tuple)
            } for value_dependency in value_dependency_set] for visitor_entry, value_dependency_set in self.T.items()},
            'R': [str(visitor_entry) for visitor_entry in self.R],
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



    def compute_R(self):
        is_change = True
        while is_change:
            is_change = False
            add_visitor_entry_set = set()
            for visitor_entry in self.C:
                # Prima regola: funzioni che partono dallo stato iniziale
                if isinstance(visitor_entry, FunctionVisitorEntry) and visitor_entry.start_state == self.Q0:
                    add_visitor_entry_set.add(visitor_entry)
                    continue
                # Seconda regola: visitor entry raggiungibili da visitor entry già inseriti
                if visitor_entry.start_state in {visitor_entry.end_state for visitor_entry in self.R}:
                    add_visitor_entry_set.add(visitor_entry)
            is_change = bool(add_visitor_entry_set.difference(self.R))
            self.R.update(add_visitor_entry_set)



    def reach(self, visitor_entry, state_id, loop_visitor_entry_set):
        # Stato di partenza trovato
        if visitor_entry.start_state == state_id:
            return True
        # Se trovo un loop interrompo
        if visitor_entry in loop_visitor_entry_set:
            return False
        # Calcolo tutti i visitor entry che lo raggiungono
        for previous_visitor_entry in (previous_visitor_entry for previous_visitor_entry in self.R if previous_visitor_entry.end_state == visitor_entry.start_state):
            if self.reach(previous_visitor_entry, state_id, loop_visitor_entry_set.union({
                visitor_entry
            })):
                return True
        return False



    def clear_events(self):
        is_change = True
        while is_change:
            remove_visitor_entry_set = set()
            for visitor_entry in self.R:
                match type(visitor_entry).__name__:
                    case EventVisitorEntry.__name__:
                        # Se la funzione che definisce l'evento non è presente rimuovo subito
                        if self.Gamma[visitor_entry] not in self.R:
                            remove_visitor_entry_set.add(visitor_entry)
                            continue
                        # Prima regola: rimuovo quando l'evento non è raggiungibile dalla funzione che lo definisce
                        if not self.reach(visitor_entry, self.Gamma[visitor_entry].end_state, set()):
                            remove_visitor_entry_set.add(visitor_entry)
                    case FunctionVisitorEntry.__name__:
                        # Seconda regola: rimuovo quando non c'è niente che precede la funzione
                        if not self.reach(visitor_entry, self.Q0, set()):
                            remove_visitor_entry_set.add(visitor_entry)
            is_change = bool(remove_visitor_entry_set)
            self.R = self.R.difference(remove_visitor_entry_set)



    def compute_RC(self):
        # Precalcolo per il passo zero
        self.RC = {visitor_entry: ({
            (
                visitor_entry,
            )
        } if isinstance(visitor_entry, FunctionVisitorEntry) and visitor_entry.start_state == self.Q0 else set()) for visitor_entry in self.R}
        is_change = True
        while is_change:
            is_change = False
            for visitor_entry in self.R:
                add_visitor_entry_tuple_set = set()
                # Considero tutte le transizioni precedenti a quella attuale
                for previous_visitor_entry in (previous_visitor_entry for previous_visitor_entry in self.R if previous_visitor_entry.end_state == visitor_entry.start_state):
                    # Inserisco le tuple necessarie senza ripetizioni all'interno, per gli eventi deve essere presente anche la funzione che li definisce
                    add_visitor_entry_tuple_set.update({(
                        *visitor_entry_tuple,
                        *((
                            visitor_entry,
                        ) if visitor_entry not in visitor_entry_tuple else ())
                    ) for visitor_entry_tuple in self.RC[previous_visitor_entry] if isinstance(visitor_entry, FunctionVisitorEntry) or self.Gamma[visitor_entry] in visitor_entry_tuple})
                is_change = is_change or bool(add_visitor_entry_tuple_set.difference(self.RC[visitor_entry]))
                self.RC[visitor_entry].update(add_visitor_entry_tuple_set)



    # TODO DSE questa funzione, in assenza di cicli, non deve fare la sommatoria in tempi di tutti gli eventi dell'abstract computation ma solamente dell'evento in esame
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
                value_dependency.value += self.t[event_visitor_entry] + functools.reduce(lambda a, b: a + b, (self.field_id_map[field_id] for field_id in self.dependency_t_map[event_visitor_entry] if field_id != NOW and self.field_id_map[event_visitor_entry] is not None), timedelta(seconds=0))
                value_dependency.dependency_tuple = tuple(sorted([
                    *value_dependency.dependency_tuple,
                    *(field_id for field_id in self.dependency_t_map[event_visitor_entry] if field_id != NOW and self.field_id_map[field_id] is None)
                ]))
        return value_dependency



    def compute_T(self):
        for visitor_entry in self.R:
            self.T[visitor_entry] = {self.Theta(visitor_entry_tuple) for visitor_entry_tuple in self.RC[visitor_entry]}



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



    def clear_time(self):
        # TODO DSE forse questi insiemi vanno ricalcolati ogni volta, attenzione perché T dovrà essere sbiancato a ogni ricalcolo
        self.compute_RC()
        self.compute_T()
        is_change = True
        while is_change:
            is_change = False
            remove_visitor_entry_set = set()
            for visitor_entry in self.R:
                match type(visitor_entry).__name__:
                    case EventVisitorEntry.__name__:
                        # Se la funzione che definisce l'evento non è presente rimuovo subito
                        if self.Gamma[visitor_entry] not in self.R:
                            remove_visitor_entry_set.add(visitor_entry)
                            continue
                        # TODO DSE X regola: rimuovo quando l'evento non è raggiungibile dalla funzione che lo definisce
                        if not self.reach(visitor_entry, self.Gamma[visitor_entry].end_state, set()):
                            remove_visitor_entry_set.add(visitor_entry)
                            continue
                        # TODO DSE X regola: controllo la solvability dei tempi
                        is_executable = False
                        for previous_visitor_entry in (previous_visitor_entry for previous_visitor_entry in self.R if previous_visitor_entry.end_state == visitor_entry.start_state):
                            for previous_value_dependency in self.T[previous_visitor_entry]:
                                for value_dependency in self.T[visitor_entry]:
                                    if self.is_solvable(previous_value_dependency, value_dependency):
                                        is_executable = True
                                        break
                                if is_executable:
                                    break
                            if is_executable:
                                break
                        if is_executable:
                            continue
                        remove_visitor_entry_set.add(visitor_entry)
                    case FunctionVisitorEntry.__name__:
                        # TODO DSE X regola: rimuovo quando non c'è niente che precede la funzione
                        if not self.reach(visitor_entry, self.Q0, set()):
                            remove_visitor_entry_set.add(visitor_entry)
            is_change = bool(remove_visitor_entry_set)
            self.R = self.R.difference(remove_visitor_entry_set)


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



    def compute_unreachable_code(self):
        # Calcolo l'unreachable-code
        self.unreachable_code = self.C.difference(self.R)
