'''
analizer.py
'''
import sys
import antlr4

from generated.StipulaLexer import StipulaLexer
from generated.StipulaParser import StipulaParser

from classes.visitor import Visitor



if __name__ == '__main__':
    input_stream = antlr4.FileStream(sys.argv[1])
    lexer = StipulaLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = StipulaParser(stream)
    tree = parser.stipula()
    if parser.getNumberOfSyntaxErrors() > 0:
        print('Syntax errors')
        sys.exit(1)
    print('+-------------+')
    print('|   Results   |')
    print('+-------------+')
    print()
    visitor = Visitor()
    visitor_output = visitor.visit(tree)
    print(visitor_output)
    if visitor_output.warning_code:
        print()
        print('Warning code found')
    if visitor_output.expired_code:
        print()
        print('Expired code found')
    if visitor_output.dead_code:
        print()
        print('Dead code found')
