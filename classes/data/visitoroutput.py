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
        self.field_id_set = set()
        self.Q0 = None
        self.C = set()
        self.Gamma = {}
        self.dependency_t_dict = {}
        self.t = {}
        self.T = {}
        self.R = set()
        self.warning_constraint = set()
        self.warning_code = set()
        self.expired_code = {}
        self.dead_code = set()



    def __str__(self):
        return json.dumps({
            'field_id_set': list(self.field_id_set),
            'Q0': self.Q0,
            'C': [str(visitor_entry) for visitor_entry in self.C],
            'Gamma': {str(event_visitor_entry): str(function_visitor_entry) for event_visitor_entry, function_visitor_entry in self.Gamma.items()},
            'dependency_t_dict': {str(visitor_entry): list(field_id_set) for visitor_entry, field_id_set in self.dependency_t_dict.items()},
            't': {str(visitor_entry): str(time_delta) for visitor_entry, time_delta in self.t.items()},
            'T': {str(visitor_entry): {
                'value': str(value_dependency.value),
                'dependency_set': list(value_dependency.dependency_set)
            } for visitor_entry, value_dependency in self.T.items()},
            'R': [str(visitor_entry) for visitor_entry in self.R],
            'warning_constraint': [[list(dependency_tuple_1), list(dependency_tuple_2)] for dependency_tuple_1, dependency_tuple_2 in self.warning_constraint],
            'warning_code': [[str(visitor_entry_1), str(visitor_entry_2)] for visitor_entry_1, visitor_entry_2 in self.warning_code],
            'expired_code': {str(visitor_entry): date_str for visitor_entry, date_str in self.expired_code.items()},
            'dead_code': [str(visitor_entry) for visitor_entry in self.dead_code]
        }, indent=2)
    


    def add_field_id(self, field_id):
        self.field_id_set.add(field_id)



    def add_visitor_entry(self, visitor_entry):
        self.C.add(visitor_entry)



    def add_event_definition(self, event_visitor_entry, function_visitor_entry):
        self.Gamma[event_visitor_entry] = function_visitor_entry



    def add_dependency_t(self, event_visitor_entry, field_id_set):
        if event_visitor_entry not in self.dependency_t_dict:
            self.dependency_t_dict[event_visitor_entry] = set()
        self.dependency_t_dict[event_visitor_entry].update(field_id_set)



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



    def is_path_from_function(self, visitor_entry, function_visitor_entry, loop_visitor_entry_set):
        # Se trovo un loop interrompo
        if visitor_entry in loop_visitor_entry_set:
            return False
        # Calcolo tutti i visitor entry che lo raggiungono
        previous_visitor_entry_set = {previous_visitor_entry for previous_visitor_entry in self.R if previous_visitor_entry.end_state == visitor_entry.start_state}
        # Verifico se ho trovato la funzione
        if function_visitor_entry in previous_visitor_entry_set:
            return True
        for previous_visitor_entry in previous_visitor_entry_set:
            # Passo successivo della ricerca
            if self.is_path_from_function(previous_visitor_entry, function_visitor_entry, loop_visitor_entry_set.union({visitor_entry})):
                return True
        return False



    def clear_events(self):
        is_change = True
        while is_change:
            remove_visitor_entry_set = set()
            for visitor_entry in self.R:
                if isinstance(visitor_entry, EventVisitorEntry):
                    # Se la funzione che definisce l'evento non è presente rimuovo subito
                    if self.Gamma[visitor_entry] not in self.R:
                        remove_visitor_entry_set.add(visitor_entry)
                        continue
                    # Prima regola: rimuovo quando l'evento non è raggiungibile dalla funzione che lo definisce
                    if not self.is_path_from_function(visitor_entry, self.Gamma[visitor_entry], set()):
                        remove_visitor_entry_set.add(visitor_entry)
                # Seconda regola: rimuovo quando non c'è niente che precede la funzione
                if isinstance(visitor_entry, FunctionVisitorEntry) and visitor_entry.start_state != self.Q0 and visitor_entry.start_state not in {visitor_entry.end_state for visitor_entry in self.R}:
                    remove_visitor_entry_set.add(visitor_entry)
            is_change = bool(remove_visitor_entry_set)
            self.R = self.R.difference(remove_visitor_entry_set)



    def compute_stipula_time(self, visitor_entry, loop_visitor_entry_set):
        #Il valore è già calcolato
        if visitor_entry in self.T:
            return
        if isinstance(visitor_entry, FunctionVisitorEntry):
            # Prima regola: funzione che parte dallo stato iniziale
            if visitor_entry.start_state == self.Q0:
                self.T[visitor_entry] = ValueDependency(timedelta(seconds=0), set())
                return
            # Seconda regola: funzione che fa parte del suo stesso loop
            if visitor_entry in loop_visitor_entry_set:
                raise LoopException(visitor_entry)
            # Controllo che tutte le dipendenze abbiano lo stipula time calcolato
            previous_visitor_entry_set = set()
            for previous_visitor_entry in (previous_visitor_entry for previous_visitor_entry in self.R if previous_visitor_entry.end_state == visitor_entry.start_state):
                try:
                    self.compute_stipula_time(previous_visitor_entry, loop_visitor_entry_set.union({visitor_entry}))
                    previous_visitor_entry_set.add(previous_visitor_entry)
                except LoopException:
                    pass
            # Se tutte i visitor entry sono loop propago l'eccezione
            if not previous_visitor_entry_set:
                raise LoopException(visitor_entry)
            # Terza regola: il tempo stipula dipende dai tempi stipula dei visitor entry entranti
            self.T[visitor_entry] = ValueDependency(min(self.T[previous_visitor_entry].value for previous_visitor_entry in previous_visitor_entry_set), functools.reduce(lambda a, b: a.union(b), (self.T[previous_visitor_entry].dependency_set for previous_visitor_entry in previous_visitor_entry_set), set()))
            return
        # Quarta regola: per gli eventi bisogna considerare la dipendenza dalla funzione che li definisce
        self.compute_stipula_time(self.Gamma[visitor_entry], set())
        self.T[visitor_entry] = ValueDependency(self.t[visitor_entry], self.dependency_t_dict.get(visitor_entry, set()).difference({NOW}))
        if NOW in self.dependency_t_dict.get(visitor_entry, set()):
            self.T[visitor_entry].value += self.T[self.Gamma[visitor_entry]].value



    def compute_T(self):
        for visitor_entry in self.R:
            self.compute_stipula_time(visitor_entry, set())



    def clear_time(self):
        is_change = True
        while is_change:
            remove_visitor_entry_set = set()
            for visitor_entry in self.R:
                if isinstance(visitor_entry, EventVisitorEntry):
                    # Se la funzione che definisce l'evento non è presente rimuovo subito
                    if self.Gamma[visitor_entry] not in self.R:
                        remove_visitor_entry_set.add(visitor_entry)
                        continue
                    # Prima regola: rimuovo quando l'evento non è raggiungibile dalla funzione che lo definisce
                    if not self.is_path_from_function(visitor_entry, self.Gamma[visitor_entry], set()):
                        remove_visitor_entry_set.add(visitor_entry)
                        continue
                    # Seconda regola: rimuovo quando non c'è nessun visitor entry entrante con stipula time minore
                    is_executable = False
                    for previous_visitor_entry in (previous_visitor_entry for previous_visitor_entry in self.R if previous_visitor_entry.end_state == visitor_entry.start_state):
                        # La certezza di dead-code è solo se tutte le dipendenze sono confrontabili
                        if self.T[previous_visitor_entry].dependency_set.difference(self.T[visitor_entry].dependency_set) or self.T[visitor_entry].dependency_set.difference(self.T[previous_visitor_entry].dependency_set):
                            is_executable = True
                            break
                        if self.T[previous_visitor_entry].value <= self.T[visitor_entry].value:
                            is_executable = True
                            break
                    if not is_executable:
                        remove_visitor_entry_set.add(visitor_entry)
                # Terza regola: rimuovo la funzione se non c'è niente che la precede
                if isinstance(visitor_entry, FunctionVisitorEntry) and visitor_entry.start_state != self.Q0 and visitor_entry.start_state not in {visitor_entry.end_state for visitor_entry in self.R}:
                    remove_visitor_entry_set.add(visitor_entry)
            is_change = bool(remove_visitor_entry_set)
            self.R = self.R.difference(remove_visitor_entry_set)



    def compute_warning_constraint(self):
        for visitor_entry in (visitor_entry for visitor_entry in self.R if visitor_entry.start_state != self.Q0):
            for previous_visitor_entry in (previous_visitor_entry for previous_visitor_entry in self.R if previous_visitor_entry.end_state == visitor_entry.start_state and self.T[previous_visitor_entry].value <= self.T[visitor_entry].value):
                previous_dependency_diff_set = self.T[previous_visitor_entry].dependency_set.difference(self.T[visitor_entry].dependency_set)
                if previous_dependency_diff_set:
                    self.warning_constraint.add((tuple(previous_dependency_diff_set), tuple(self.T[visitor_entry].dependency_set.difference(self.T[previous_visitor_entry].dependency_set)), ))



    def compute_warning_code(self):
        for event_visitor_entry in (event_visitor_entry for event_visitor_entry in self.R if isinstance(event_visitor_entry, EventVisitorEntry)):
            self.warning_code.update({(previous_visitor_entry, event_visitor_entry, ) for previous_visitor_entry in self.R if previous_visitor_entry.end_state == event_visitor_entry.start_state and self.T[previous_visitor_entry].value > self.T[event_visitor_entry].value})



    def set_expired_code(self, event_visitor_entry, date_str):
        # Identifico un evento come expired
        self.expired_code[event_visitor_entry] = date_str



    def compute_dead_code(self):
        # Calcolo il dead code
        self.dead_code = self.C.difference(self.R)
