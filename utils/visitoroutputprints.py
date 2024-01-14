'''
visitoroutputprints.py
'''
import json

from classes.data.functionvisitorentry import FunctionVisitorEntry



def _str_function_visitor_entry(function_visitor_entry):
    return f"{function_visitor_entry.start_state} {function_visitor_entry.handler}.{function_visitor_entry.code_id} {function_visitor_entry.end_state}"



def _str_event_visitor_entry(event_visitor_entry):
    return f"{event_visitor_entry.start_state} ev.{event_visitor_entry.code_id} {event_visitor_entry.end_state}"



def str_visitor_entry(visitor_entry):
    if isinstance(visitor_entry, FunctionVisitorEntry):
        return _str_function_visitor_entry(visitor_entry)
    return _str_event_visitor_entry(visitor_entry)



def print_visitor_output(visitor_output):
    print(json.dumps({
        'field_id_set': list(visitor_output.field_id_set),
        'Q0': visitor_output.Q0,
        'C': [str_visitor_entry(visitor_entry) for visitor_entry in visitor_output.C],
        'Gamma': {str_visitor_entry(event_visitor_entry): str_visitor_entry(function_visitor_entry) for event_visitor_entry, function_visitor_entry in visitor_output.Gamma.items()},
        'dependency_t_dict': {str_visitor_entry(visitor_entry): list(field_id_set) for visitor_entry, field_id_set in visitor_output.dependency_t_dict.items()},
        't': {str_visitor_entry(visitor_entry): str(time_delta) for visitor_entry, time_delta in visitor_output.t.items()},
        'T': {str_visitor_entry(visitor_entry): {
            'value': str(value_dependency.value),
            'dependency_set': list(value_dependency.dependency_set)
        } for visitor_entry, value_dependency in visitor_output.T.items()},
        'R': {state: [str_visitor_entry(visitor_entry) for visitor_entry in visitor_entry_set] for state, visitor_entry_set in visitor_output.R.items()},
        'warning_constraint': [f"{field_id_1} <= {field_id_2}" for field_id_1, field_id_2 in visitor_output.warning_constraint],
        'warning_code': [f"{str_visitor_entry(visitor_entry_1)} -> {str_visitor_entry(visitor_entry_2)}" for visitor_entry_1, visitor_entry_2 in visitor_output.warning_code],
        'expired_code': {str_visitor_entry(visitor_entry): date_str for visitor_entry, date_str in visitor_output.expired_code.items()},
        'dead_code': [str_visitor_entry(visitor_entry) for visitor_entry in visitor_output.dead_code]
    }, indent=2))
