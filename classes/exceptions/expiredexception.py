'''
expiredexception.py
'''
class ExpiredException(Exception):



    def __init__(self, date_str):
        Exception.__init__(self, f"`{date_str}` is expired")
        self.date_str = date_str
