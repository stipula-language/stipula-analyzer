'''
visitoroutput.py
'''
import json

from classes.exceptions.loopexception import LoopException
from classes.data.functionvisitorentry import FunctionVisitorEntry
from classes.data.eventvisitorentry import EventVisitorEntry



class VisitorOutput:



    def __init__(self):
        self.field_id_set = set()
        self.Q0 = None
        self.C = set()
        self.Gamma = {}
        self.dependency_t_dict = {}
        self.t = {}
        self.Ts = {}
        self.R = {}
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
            't': {str(visitor_entry): time_delta for visitor_entry, time_delta in self.t.items()},
            'Ts': {str(event_visitor_entry): stipula_time for event_visitor_entry, stipula_time in self.Ts.items()},
            'R': {state: [str(visitor_entry) for visitor_entry in visitor_entry_set] for state, visitor_entry_set in self.R.items()},
            'warning_code': [f"{str(visitor_entry_1)} -> {str(visitor_entry_2)}" for visitor_entry_1, visitor_entry_2 in self.warning_code],
            'expired_code': {str(visitor_entry): date_str for visitor_entry, date_str in self.expired_code.items()},
            'dead_code': [str(visitor_entry) for visitor_entry in self.dead_code]
        }, indent=2)



    def add_event_definition(self, event_visitor_entry, function_visitor_entry):
        self.Gamma[event_visitor_entry] = function_visitor_entry



    def add_visitor_entry(self, visitor_entry):
        # Aggiungo la entry al codice
        self.C.add(visitor_entry)
        # Check esistenza dell'insieme
        if visitor_entry.start_state not in self.R:
            self.R[visitor_entry.start_state] = set()
        # Aggiungo la entry all'insieme dello stato di partenza
        self.R[visitor_entry.start_state].add(visitor_entry)
        # Aggiungo la entry in tutti gli insiemi che può raggiungere
        for visitor_entry_set in self.R.values():
            is_add = False
            for previous_visitor_entry in visitor_entry_set:
                if previous_visitor_entry.end_state == visitor_entry.start_state:
                    is_add = True
            if is_add:
                visitor_entry_set.add(visitor_entry)



    def clear_events(self):
        # Rimuovo tutti gli eventi non raggiungibili dalla funzione che li definisce
        for visitor_entry_set in self.R.values():
            for event_visitor_entry in {visitor_entry for visitor_entry in visitor_entry_set if isinstance(visitor_entry, EventVisitorEntry)}:
                if event_visitor_entry not in self.R.get(self.Gamma[event_visitor_entry].end_state, set()):
                    visitor_entry_set.remove(event_visitor_entry)
        # Rimuovo tutte le entry scollegate all'interno degli insiemi
        for state, visitor_entry_set in self.R.items():
            is_change = True
            while is_change:
                is_change = False
                for visitor_entry in {visitor_entry for visitor_entry in visitor_entry_set if visitor_entry.start_state != state}:
                    if visitor_entry.start_state not in {visitor_entry.end_state for visitor_entry in visitor_entry_set}:
                        is_change = True
                        visitor_entry_set.remove(visitor_entry)



    def compute_stipula_time(self, visitor_entry, loop_visitor_entry):
        # Il valore è già calcolato
        if visitor_entry in self.Ts:
            return
        # Partenza dallo stato iniziale
        if isinstance(visitor_entry, FunctionVisitorEntry) and visitor_entry.start_state == self.Q0:
            self.Ts[visitor_entry] = 0
            return
        # Ho trovato un loop
        if visitor_entry == loop_visitor_entry:
            raise LoopException(visitor_entry)
        # Controllo che tutte le dipendenze abbiano lo stipula time calcolato, il flag indica la presenza di una LoopException
        previous_visitor_entry_dict = {previous_visitor_entry: False for previous_visitor_entry in self.R[self.Q0] if previous_visitor_entry.end_state == visitor_entry.start_state}
        for previous_visitor_entry in previous_visitor_entry_dict:
            try:
                self.compute_stipula_time(previous_visitor_entry, loop_visitor_entry or visitor_entry)
            except LoopException:
                previous_visitor_entry_dict[previous_visitor_entry] = True
        # Se sono tutti loop propago l'eccezione
        previous_visitor_entry_set = {previous_visitor_entry for previous_visitor_entry, is_loop_exception in previous_visitor_entry_dict.items() if not is_loop_exception}
        if not previous_visitor_entry_set:
            raise LoopException(visitor_entry)
        # Calcolo lo stipula time
        if isinstance(visitor_entry, FunctionVisitorEntry):
            self.Ts[visitor_entry] = min(self.Ts[previous_visitor_entry] for previous_visitor_entry in previous_visitor_entry_set)
            return
        if isinstance(visitor_entry, EventVisitorEntry) and not self.dependency_t_dict[visitor_entry]:
            self.Ts[visitor_entry] = self.Ts[self.Gamma[visitor_entry]] + self.t[visitor_entry]



    def compute_Ts(self):
        for visitor_entry in self.R[self.Q0]:
            self.compute_stipula_time(visitor_entry, None)



    # TODO DSE in questo passaggio devo considerare le dipendenze tra i field per poter imporre condizioni di warning sull'eseguibilità del codice
    # TODO DSE forse è necessatio verificare anche se il field va aggiunto a now perché andrebbe a rappresentare un delta e non un valore assoluto
    def clear_time(self):
        # Rimuovo il codice non eseguibile e segnalo quello non sempre eseguibile
        remove_visitor_entry_set = set()
        for visitor_entry in self.R[self.Q0]:
            previous_visitor_entry_set = {previous_visitor_entry for previous_visitor_entry in self.R[self.Q0] if previous_visitor_entry.end_state == visitor_entry.start_state}
            if not previous_visitor_entry_set:
                continue
            is_uncertain = False
            is_executable = False
            warning_code = set()
            for previous_visitor_entry in previous_visitor_entry_set:
                if (self.dependency_t_dict[previous_visitor_entry] if isinstance(previous_visitor_entry, EventVisitorEntry) else False) or (self.dependency_t_dict[visitor_entry] if isinstance(visitor_entry, EventVisitorEntry) else False):
                    is_uncertain = True
                    warning_code.add((previous_visitor_entry, visitor_entry, ))
                    continue
                if self.Ts[previous_visitor_entry] <= self.Ts[visitor_entry]:
                    is_executable = True
                    continue
                warning_code.add((previous_visitor_entry, visitor_entry, ))
            if is_uncertain or is_executable:
                self.warning_code.update(warning_code)
                continue
            remove_visitor_entry_set.add(visitor_entry)
        self.R[self.Q0] = self.R[self.Q0].difference(remove_visitor_entry_set)



    def compute_dead_code(self):
        # Calcolo il dead code
        self.dead_code = self.C.difference(self.R[self.Q0])
