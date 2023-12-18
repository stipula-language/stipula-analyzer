'''
fieldexception.py
'''
class FieldException(Exception):



    def __init__(self, field_id):
        Exception.__init__(self, f"`{field_id}` is a field")
        self.field_id = field_id
