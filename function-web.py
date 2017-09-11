from pathlib import Path
import re
import test2 as function_file
import pandas as pd
from http.server import HTTPServer, CGIHTTPRequestHandler

method_names = dir(function_file)
function_dict = {}
def_re = 'def.*?\('
def_names = []
contents = Path('test2.py').read_text()

# break contents by \n
split_contents = contents.split('\n')

in_function = False
function_name = None

# create dictionary with functions as keys and their links as values
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

# create dataframe with sources and targets
source_list = []
target_list = []
for key, value in function_dict.items():
    for element in value:
        source_list.append(key)
        target_list.append(element)
dataframe = pd.DataFrame(data={'source': source_list, 'target': target_list})

# write to CSV
dataframe.to_csv('function-data.csv')


# start the local server so that d3 can read CSV
port = 8000
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
print("Go to http://localhost:8000/network-graph.html to view function network graph.")
httpd.serve_forever()




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
