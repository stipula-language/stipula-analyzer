'''
visitoroutput.py
'''
from datetime import timedelta
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
        self.R = {}
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
            'T': {str(event_visitor_entry): {
                'value': str(value_dependency.value),
                'dependency_set': list(value_dependency.dependency_set)
            } for event_visitor_entry, value_dependency in self.T.items()},
            'R': {state: [str(visitor_entry) for visitor_entry in visitor_entry_set] for state, visitor_entry_set in self.R.items()},
            'warning_constraint': [f"{field_id_1} <= {field_id_2}" for field_id_1, field_id_2 in self.warning_constraint],
            'warning_code': [f"{str(visitor_entry_1)} -> {str(visitor_entry_2)}" for visitor_entry_1, visitor_entry_2 in self.warning_code],
            'expired_code': {str(visitor_entry): date_str for visitor_entry, date_str in self.expired_code.items()},
            'dead_code': [str(visitor_entry) for visitor_entry in self.dead_code]
        }, indent=2)



    def add_event_definition(self, event_visitor_entry, function_visitor_entry):
        self.Gamma[event_visitor_entry] = function_visitor_entry



    def add_visitor_entry(self, visitor_entry):
        # Aggiungo la entry al codice
        self.C.add(visitor_entry)
        # Controllo l'esistenza dell'insieme
        if not visitor_entry.start_state in self.R:
            self.R[visitor_entry.start_state] = set()
        # Aggiungo la entry all'insieme dello stato di partenza e inserisco anche l'insieme dello stato di arrivo
        self.R[visitor_entry.start_state].update({visitor_entry}, self.R.get(visitor_entry.end_state, set()))
        # Aggiungo la entry in tutti gli insiemi che può raggiungere inserendo l'insieme di raggiungibilità dello stato di partenza
        for visitor_entry_set in self.R.values():
            is_add = False
            for previous_visitor_entry in visitor_entry_set:
                if previous_visitor_entry.end_state == visitor_entry.start_state:
                    is_add = True
            if is_add:
                visitor_entry_set.update(self.R[visitor_entry.start_state])



    def clear_holes(self, state):
        # Rimuovo tutte le entry scollegate all'interno dell'insieme
        is_change = True
        while is_change:
            is_change = False
            for visitor_entry in {visitor_entry for visitor_entry in self.R[state] if visitor_entry.start_state != state}:
                if visitor_entry.start_state not in {visitor_entry.end_state for visitor_entry in self.R[state]}:
                    is_change = True
                    self.R[state].remove(visitor_entry)



    def clear_events(self):
        # Rimuovo tutti gli eventi non raggiungibili dalla funzione che li definisce
        for visitor_entry_set in self.R.values():
            for event_visitor_entry in {visitor_entry for visitor_entry in visitor_entry_set if isinstance(visitor_entry, EventVisitorEntry)}:
                if event_visitor_entry not in self.R.get(self.Gamma[event_visitor_entry].end_state, set()):
                    visitor_entry_set.remove(event_visitor_entry)
        # Ripulisco tutti gli insiemi di raggiungibilità in base ai buchi generati
        for state in self.R:
            self.clear_holes(state)



    def compute_stipula_time(self, visitor_entry, loop_visitor_entry_set):
        # Il valore è già calcolato
        if visitor_entry in self.T:
            return
        # Partenza dallo stato iniziale
        if isinstance(visitor_entry, FunctionVisitorEntry) and visitor_entry.start_state == self.Q0:
            self.T[visitor_entry] = ValueDependency(timedelta(seconds=0), set())
            return
        # Ho trovato un loop
        if visitor_entry in loop_visitor_entry_set:
            raise LoopException(visitor_entry)
        # Controllo che tutte le dipendenze abbiano lo stipula time calcolato, il flag indica la presenza di una LoopException
        previous_visitor_entry_dict = {previous_visitor_entry: False for previous_visitor_entry in self.R[self.Q0] if previous_visitor_entry.end_state == visitor_entry.start_state}
        for previous_visitor_entry in previous_visitor_entry_dict:
            try:
                self.compute_stipula_time(previous_visitor_entry, loop_visitor_entry_set.union({visitor_entry}))
            except LoopException:
                previous_visitor_entry_dict[previous_visitor_entry] = True
        # Se sono tutti loop propago l'eccezione
        previous_visitor_entry_set = {previous_visitor_entry for previous_visitor_entry, is_loop_exception in previous_visitor_entry_dict.items() if not is_loop_exception}
        if not previous_visitor_entry_set:
            raise LoopException(visitor_entry)
        # Calcolo lo stipula time
        if isinstance(visitor_entry, FunctionVisitorEntry):
            dependency_set = set()
            for previous_visitor_entry in previous_visitor_entry_set:
                dependency_set.union(self.T[previous_visitor_entry].dependency_set)
            self.T[visitor_entry] = ValueDependency(min(self.T[previous_visitor_entry].value for previous_visitor_entry in previous_visitor_entry_set), dependency_set)
            return
        if isinstance(visitor_entry, EventVisitorEntry):
            value_dependency = ValueDependency(self.t[visitor_entry], self.dependency_t_dict.get(visitor_entry, set()).difference({NOW}))
            # In caso di eventi devo valutare se il calcolo parte da now o se è una data assoluta
            if NOW in self.dependency_t_dict.get(visitor_entry, set()):
                value_dependency.value += self.T[self.Gamma[visitor_entry]].value
            self.T[visitor_entry] = value_dependency



    def compute_Ts(self):
        for visitor_entry in self.R[self.Q0]:
            self.compute_stipula_time(visitor_entry, set())



    def clear_time(self):
        # Rimuovo il codice non eseguibile e segnalo quello non sempre eseguibile
        remove_visitor_entry_set = set()
        for visitor_entry in (visitor_entry for visitor_entry in self.R[self.Q0] if visitor_entry.start_state != self.Q0):
            previous_visitor_entry_set = {previous_visitor_entry for previous_visitor_entry in self.R[self.Q0] if previous_visitor_entry.end_state == visitor_entry.start_state}
            is_executable = False
            warning_code = set()
            for previous_visitor_entry in previous_visitor_entry_set:
                # Considero lo stipula time
                if self.T[previous_visitor_entry].value <= self.T[visitor_entry].value:
                    is_executable = True
                    # Controllo che le dipendenze siano confrontabili
                    previous_dependency_set = self.T[previous_visitor_entry].dependency_set.difference(self.T[visitor_entry].dependency_set)
                    if previous_dependency_set:
                        dependency_set = self.T[visitor_entry].dependency_set.difference(self.T[previous_visitor_entry].dependency_set)
                        for previous_field_id in previous_dependency_set:
                            # Se il codice successivo non usa dipendenze allora quelle precedenti potrebbero dover essere azzerate
                            if not dependency_set:
                                self.warning_constraint.add((previous_field_id, 0, ))
                                continue
                            for field_id in self.T[visitor_entry].dependency_set.difference(self.T[previous_visitor_entry].dependency_set):
                                self.warning_constraint.add((previous_field_id, field_id, ))
                    continue
                warning_code.add((previous_visitor_entry, visitor_entry, ))
            if is_executable:
                self.warning_code.update(warning_code)
                continue
            remove_visitor_entry_set.add(visitor_entry)
        self.R[self.Q0] = self.R[self.Q0].difference(remove_visitor_entry_set)
        # Ripulisco l'insieme di raggiugibilità dai buchi creati
        self.clear_holes(self.Q0)



    def compute_dead_code(self):
        # Calcolo il dead code
        self.dead_code = self.C.difference(self.R[self.Q0])
