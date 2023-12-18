'''
functionvisitorentry.py
'''
from classes.data.visitorentry import VisitorEntry



class FunctionVisitorEntry(VisitorEntry):



    def __str__(self):
        return f"fn{VisitorEntry.__str__(self)}"
