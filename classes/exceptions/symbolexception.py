'''
symbolexception.py
'''
class SymbolException(Exception):



    def __init__(self, symbol):
        Exception.__init__(self, f"`{symbol}` is not a valid symbol")
