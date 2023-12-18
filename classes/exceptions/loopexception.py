'''
loopexception.py
'''
class LoopException(Exception):



    def __init__(self, visitor_entry):
        Exception.__init__(self, f"Loop detected for `{str(visitor_entry)}`")
