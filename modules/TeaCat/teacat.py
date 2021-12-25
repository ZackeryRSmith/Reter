#!/usr/bin/env python
###########################################################################     
#                                                                         #     
#                             TeaCat (Super Cat!)                         #     
#                                      ~ A pretifyed version of the cat   #     
#                                                                         #     
#  Copyright (c) 2020, Zackery .R. Smith <zackery.smith82307@gmail.com>.  #     
#                                                                         #     
#  This program is free software: you can redistribute it and/or modify   #     
#  it under the terms of the GNU General Public License as published by   #     
#  the Free Software Foundation, either version 3 of the License, or      #     
#  (at your option) any later version.                                    #     
#                                                                         #     
#  This program is distributed in the hope that it will be useful,        #     
#  but WITHOUT ANY WARRANTY; without even the implied warranty of         #     
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #     
#  GNU General Public License for more details.                           #     
#                                                                         #     
#  You should have received a copy of the GNU General Public License      #     
#  along with this program. If not, see <http://www.gnu.org/licenses/>.   #     
#                                                                         #     
###########################################################################
                        #  Proudly written in Vim  #
                        #    Zackery .R. Smith     #
                        # github.com/ZackeryRSmith #
                        ############################



__author__ = "Zackery Smith"
__email__ = "zackery.smith82307@gmail.com"
__copyright__ = "Copyright © 2020 Zackery Smith. All rights reserved."
__license__ = "GNU GPL-3.0"
__version_info__ = (0, 0, 1)
__version__ = ".".join(map(str, __version_info__))


import os
import sys
sys.path.append("../../")
import argparse
from reter.reter import (
    init,
    indicator,
    captureKey
)
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Match,
    Optional,
    Pattern,
    Sequence,
    Set,
    TextIO,
    Tuple,
    Union,
    cast,
)


########################################
# TEACAT
########################################

terminal = init()
parser = argparse.ArgumentParser(description='TeaCat is a prettier version of the unix command cat. Out of the box it comes with script highlighting for python, javascript, rust, c, c++, c#, and sh! Along with line numbers, a file tree, and additonal file info. TeaCat also has plugin system so anyone can improve upon it!')

# Create args
parser.add_argument("Path", metavar='path', type=str,
                    help="The path to file (Does work with relative paths!)")

parser.add_argument("-s", action="store_true", default=True,
                    dest="syntax_highlight",
                    help="Syntax highlighting")

parser.add_argument("-t", action="store_true", default=True,
                    dest="file_tree",
                    help="Display file tree")

parser.add_argument("--noargs", action="store_true", default=False,
                    dest="noargs",
                    help="Disables all default args")

# Parse args
args = parser.parse_args()

# Create argument variables
passedPath = args.Path

# Create sub variables
fd = None  # Set later on 

# Get initial pos
initPos = terminal.cursor.getPos()

# Check if given path is a folder or file
if not os.path.isdir(passedPath):
    if os.path.isfile(passedPath):
        fd = "file"
    else:
        print('The path specified does not exist')
        sys.exit()
else:
    fd = "folder"

# IF file descripter is a folder
if fd == "folder":
    pass
else:
    fileContents = ""
    # Read file
    with open(passedPath, "r") as passedFile:
        fileContents = passedFile.read()
    # Print the number of lines the screen can hold
    #sys.__stdout__.write(fileContents)
    while True:  # Keep file running
        pass
