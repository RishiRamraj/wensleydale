"""Parse python code into the abstract syntax tree and represent as JSON"""
from __future__ import print_function
import ast
from itertools import chain, count
import json
import sys


def dictify(obj):
    if hasattr(obj, "__dict__"):
        result = {k: dictify(v) for k, v in chain(obj.__dict__.items(), [("classname", obj.__class__.__name__)])}
        return result
    elif isinstance(obj, list):
        return [dictify(x) for x in obj]
    else:
        return obj


def parse_file(filename):
    with open(filename) as f:
        source = f.read()
        return ast.parse(source, filename=filename, mode="exec")


def main(args):
    filename = args[0]
    if len(args) != 1 or filename.lower() in ("help", "h", "-h", "--help"):
        print(__doc__)
    else:
        ast_node = parse_file(filename)
        ast_dict = dictify(ast_node) 
        ast_json = json.dumps(ast_dict, sort_keys=True, indent=4, separators=(',', ': '))
        print(ast_json)

if __name__ == "__main__":
    main(sys.argv[1:])
