'''
visitorentry.py
'''
class VisitorEntry:



    def __init__(self, start_state, handler, code_id, end_state, code_reference):
        self.start_state = start_state
        self.handler = handler
        self.code_id = code_id
        self.end_state = end_state
        self.code_reference = code_reference



    def __str__(self):
        return str((
            self.start_state,
            self.handler,
            self.code_id,
            self.end_state,
        ))
