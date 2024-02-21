'''
analyzer.py
'''
import sys
import re
import antlr4
import click

from generated.StipulaLexer import StipulaLexer
from generated.StipulaParser import StipulaParser

from classes.visitor import Visitor
from utils import visitoroutputprints



def _print_constraint(dependency_tuple):
    if not dependency_tuple:
        return '0'
    dependency_list = []
    actual_dependency = dependency_tuple[0]
    dependency_counter = 1
    for dependency in (
        *dependency_tuple[1:],
        None,
    ):
        if dependency == actual_dependency:
            dependency_counter += 1
            continue
        dependency_list.append(f"{f'{dependency_counter} ' if dependency_counter > 1 else ''}{actual_dependency}")
        actual_dependency = dependency
        dependency_counter = 1
    return ' + '.join(dependency_list)



def _clear_code(line_list):
    space_before = 0
    index = 0
    is_break = False
    while line_list[0][index] in (' ', '\t', ):
        for code_line in line_list[1:]:
            if re.sub(r'^[\r\n]+', '', code_line) and code_line[index] != line_list[0][index]:
                is_break = True
                break
        if is_break:
            break
        space_before += 1
        index += 1
    return_list = [
        *[(code_line[space_before:] if re.sub(r'^[\r\n]+', '', code_line) else code_line) for code_line in line_list[:-1]],
        line_list[-1][space_before:].rstrip()
    ]
    return return_list



def _print_code(line_list, visitor_entry, is_readable):
    line_str = f"line {visitor_entry.code_reference.start_line}:   "
    print(f"    {(visitoroutputprints.str_visitor_entry(visitor_entry) if is_readable else str(visitor_entry))} :")
    print(f"{line_str}{(' ' * len(line_str)).join(_clear_code(line_list[visitor_entry.code_reference.start_line - 1:visitor_entry.code_reference.end_line]))}")



@click.command()
@click.option('-r', '--readable', 'is_readable', type=bool, default=False, show_default=True, is_flag=True, help='Show the output human readable.')
@click.option('-c', '--compact', 'is_compact', type=bool, default=False, show_default=True, is_flag=True, help='Show only the relevant output.')
@click.argument('file-path', type=str)
def _main(is_readable, is_compact, file_path):
    input_stream = antlr4.FileStream(file_path)
    lexer = StipulaLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = StipulaParser(stream)
    tree = parser.stipula()
    if parser.getNumberOfSyntaxErrors() > 0:
        print('Syntax errors')
        sys.exit(1)
    visitor = Visitor()
    visitor_output = visitor.visit(tree)
    with open(file_path, 'r', encoding='utf-8') as file:
        line_list = file.readlines()
    print('+-------------+')
    print('|   Results   |')
    print('+-------------+')
    if is_readable:
        visitoroutputprints.print_visitor_output(visitor_output, is_compact)
    else:
        print(visitor_output)

    if visitor_output.reachability_constraint:
        print('REACHABILITY CONSTRAINT [', end=('' if len(visitor_output.reachability_constraint) == 1 and is_compact else '\n'))
        for dependency_tuple_1, dependency_tuple_2 in visitor_output.reachability_constraint:
            print(f"    {_print_constraint(dependency_tuple_1)} <= {_print_constraint(dependency_tuple_2)}{('    ' if len(visitor_output.reachability_constraint) == 1 and is_compact else '')}", end=('' if len(visitor_output.reachability_constraint) == 1 and is_compact else '\n'))
        print(']')
    if visitor_output.warning_code:
        print('WARNING CODE [', end=('' if len(visitor_output.warning_code) == 1 and is_compact else '\n'))
        for visitor_entry_1, visitor_entry_2 in visitor_output.warning_code:
            print(f"    {(visitoroutputprints.str_visitor_entry(visitor_entry_1) if is_readable else str(visitor_entry_1))} --X-> {(visitoroutputprints.str_visitor_entry(visitor_entry_2) if is_readable else str(visitor_entry_2))}{('    ' if len(visitor_output.warning_code) == 1 and is_compact else '')}", end=('' if len(visitor_output.warning_code) == 1 and is_compact else '\n'))
            if not is_compact:
                _print_code(line_list, visitor_entry_1, is_readable)
                _print_code(line_list, visitor_entry_2, is_readable)
        print(']')
    if visitor_output.expired_code:
        print('EXPIRED CODE [', end=('' if len(visitor_output.expired_code) == 1 and is_compact else '\n'))
        for visitor_entry in visitor_output.expired_code:
            if is_compact:
                print(f"    {visitoroutputprints.str_visitor_entry(visitor_entry)}{('    ' if len(visitor_output.expired_code) == 1 else '')}", end=('' if len(visitor_output.expired_code) == 1 else '\n'))
                continue
            _print_code(line_list, visitor_entry, is_readable)
        print(']')
    if visitor_output.unreachable_code:
        print('UNREACHABLE CODE [', end=('' if len(visitor_output.unreachable_code) == 1 and is_compact else '\n'))
        for visitor_entry in visitor_output.unreachable_code:
            if is_compact:
                print(f"    {visitoroutputprints.str_visitor_entry(visitor_entry)}{('    ' if len(visitor_output.unreachable_code) == 1 else '')}", end=('' if len(visitor_output.unreachable_code) == 1 else '\n'))
                continue
            _print_code(line_list, visitor_entry, is_readable)
        print(']')




if __name__ == '__main__':
    _main()
