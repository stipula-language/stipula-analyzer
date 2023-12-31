'''
analyzer.py
'''
import sys
import re
import antlr4

from generated.StipulaLexer import StipulaLexer
from generated.StipulaParser import StipulaParser

from classes.visitor import Visitor



def _clear_code(code_line_list):
    space_before = 0
    index = 0
    is_break = False
    while code_line_list[0][index] in (' ', '\t', ):
        for code_line in code_line_list[1:]:
            if re.sub(r'^[\r\n]+', '', code_line) and code_line[index] != code_line_list[0][index]:
                is_break = True
                break
        if is_break:
            break
        space_before += 1
        index += 1
    return_list = [
        *[(code_line[space_before:] if re.sub(r'^[\r\n]+', '', code_line) else code_line) for code_line in code_line_list[:-1]],
        code_line_list[-1][space_before:].rstrip()
    ]
    return return_list



def _print_code(code_line_list, visitor_entry):
    line_str = f"line {visitor_entry.code_reference.start_line}:   "
    print(f"=== {visitor_entry} ===")
    print(f"{line_str}{(' ' * len(line_str)).join(_clear_code(line_list[visitor_entry.code_reference.start_line - 1:visitor_entry.code_reference.end_line]))}")



if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        line_list = file.readlines()
    input_stream = antlr4.FileStream(sys.argv[1])
    lexer = StipulaLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = StipulaParser(stream)
    tree = parser.stipula()
    if parser.getNumberOfSyntaxErrors() > 0:
        print('Syntax errors')
        sys.exit(1)
    visitor = Visitor()
    visitor_output = visitor.visit(tree)
    print('+-------------+')
    print('|   Results   |')
    print('+-------------+')
    print()
    print(visitor_output)
    if visitor_output.warning_code:
        print()
        print('========== BEGIN WARNING CODE ==========')
        for visitor_entry in visitor_output.warning_code:
            print()
            _print_code(line_list, visitor_entry)
        print()
        print('========== END WARNING CODE ==========')
    if visitor_output.expired_code:
        print()
        print('========== BEGIN EXPIRED CODE ==========')
        for visitor_entry in visitor_output.expired_code:
            print()
            _print_code(line_list, visitor_entry)
        print()
        print('========== END EXPIRED CODE ==========')
    if visitor_output.dead_code:
        print()
        print('========== BEGIN DEAD CODE ==========')
        for visitor_entry in visitor_output.dead_code:
            print()
            _print_code(line_list, visitor_entry)
        print()
        print('========== END DEAD CODE ==========')
