'''
eventvisitorentry.py
'''
from classes.data.visitorentry import VisitorEntry



class EventVisitorEntry(VisitorEntry):



    def __str__(self):
        return f"ev{VisitorEntry.__str__(self)}"
