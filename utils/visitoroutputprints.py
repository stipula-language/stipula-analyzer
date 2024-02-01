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



def print_visitor_output(visitor_output, is_compact):
    print(json.dumps({
        'field_id_map': {field_id: str(value) for field_id, value in visitor_output.field_id_map.items()},
        'Q0': visitor_output.Q0,
        'C': [str_visitor_entry(visitor_entry) for visitor_entry in visitor_output.C],
        **({
            'Gamma': {str_visitor_entry(event_visitor_entry): str_visitor_entry(function_visitor_entry) for event_visitor_entry, function_visitor_entry in visitor_output.Gamma.items()}
        } if not is_compact else {}),
        **({
            'dependency_t_map': {str_visitor_entry(visitor_entry): list(field_id_tuple) for visitor_entry, field_id_tuple in visitor_output.dependency_t_map.items()}
        } if not is_compact else {}),
        **({
            't': {str_visitor_entry(visitor_entry): str(time_delta) for visitor_entry, time_delta in visitor_output.t.items()}
        } if not is_compact else {}),
        'T': {str_visitor_entry(visitor_entry): [
            ({
                'value': str(value_dependency.value),
                'dependency_tuple': list(value_dependency.dependency_tuple)
            } if not is_compact else str(value_dependency.value)) for value_dependency in value_dependency_set
        ] for visitor_entry, value_dependency_set in visitor_output.T.items()},
        'R': [str_visitor_entry(visitor_entry) for visitor_entry in visitor_output.R],
        **({
            'reachability_constraint': [[[str(dependency) for dependency in dependency_tuple_1], [str(dependency) for dependency in dependency_tuple_2]] for dependency_tuple_1, dependency_tuple_2 in visitor_output.reachability_constraint]
        } if not is_compact else {}),
        **({
            'warning_code': [f"{str_visitor_entry(visitor_entry_1)} -> {str_visitor_entry(visitor_entry_2)}" for visitor_entry_1, visitor_entry_2 in visitor_output.warning_code]
        } if not is_compact else {}),
        **({
            'expired_code': {str_visitor_entry(visitor_entry): str(time_delta) for visitor_entry, time_delta in visitor_output.expired_code.items()}
        } if not is_compact else {}),
        'unreachable_code': [str_visitor_entry(visitor_entry) for visitor_entry in visitor_output.unreachable_code]
    }, indent=2))
