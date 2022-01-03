# Frig Python Paths, a project I will most likely work on after Reter.
# Calm down it's a joke... slightly I don't like how annoying importing
# sibling modules is without the use of path relativity.

# As of now this is very simple but I have some cool ideas for this "joke".

import os
import sys
import re


file_path = os.path.realpath(__file__)


def get_master_path(master) -> str:
    path = re.findall(fr'.*{master}\/', file_path)
    try:
        return path[0]
    except IndexError:
        return f'Unable to locate "{master}"'


def set_abpath(path):
    sys.path.append(path)

