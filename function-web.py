# we need to find all function names and then one at a time figure out
# when functions are called by other functions
from pathlib import Path
import re
import test

method_names = dir(test)
function_dict = {}
def_re = 'def.*?\('
def_names = []
contents = Path('test.py').read_text()

# break contents by \n
split_contents = contents.split('\n')

in_function = False
function_name = None

for line in split_contents:
    if re.match('\s*#', line):
        continue
    search = re.search(def_re, line)
    if search is not None:
        in_function = True
        function_name = search.group()[4:-1]
        function_dict[function_name] = []
    elif search is None and in_function:
        for method in method_names:
            if method in line:
                function_dict[function_name].append(method)

print(function_dict)


# with contents.open() as f:
#     while f.readline() != '':
#         print('---------')
#         line = f.readline()
#         print(1, line)
#         t = re.search(def_re, line)
#         import pdb;pdb.set_trace()
#         if re.search(def_re, line) is not None:
#             print(2, line)
#             print(t.group())
#             print(3, line)
#             def_names.append(t.group())
#             print(4, line)

# look for def and one of the method names, then look for other method names
# until you find another def, start over

# import ast
# import sys
#
# def top_level_functions(body):
#     return (f for f in body if isinstance(f, ast.FunctionDef))
#
# def parse_ast(filename):
#     with open(filename, "rt") as file:
#         return ast.parse(file.read(), filename=filename)
#
# if __name__ == "__main__":
#     for filename in sys.argv[1:]:
#         print(filename)
#         tree = parse_ast(filename)
#         for func in top_level_functions(tree.body):
#             print("  %s" % func.name)
