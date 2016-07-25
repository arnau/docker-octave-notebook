#!/usr/bin/env python

"""
Suppress output and prompt numbers in git version control.  The notebooks
 themselves are not changed.

Taken from: http://pascalbugnion.net/blog/ipython-notebooks-and-git.html.
"""
import sys
import json

nb = sys.stdin.read()
json_in = json.loads(nb)
nb_metadata = json_in["metadata"]

def strip_output_from_cell(cell):
    if "outputs" in cell:
        cell["outputs"] = []

    if "execution_count" in cell:
        del cell["execution_count"]

for cell in json_in["cells"]:
    strip_output_from_cell(cell)

json.dump(json_in, sys.stdout, sort_keys=True, indent=1, separators=(",",": "))
