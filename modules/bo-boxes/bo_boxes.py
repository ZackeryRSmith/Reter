#!/usr/bin/env python
###########################################################################     
#                                                                         #     
#                          Bo-Boxes (Combo-Boxes)                         #     
#                                   ~ Creating combo boxes for the Unix   #
#                                        shell has never been easier      #
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

## TODO ##
# 1. Create multi-select box (selectionBox())
# 2. Create a drop-down like box (dropdownBox())
# 3. Create support for embedded choices (listBox()) 
# 4. Simplify code, mainly adding some of these features into Reter


__author__ = "Zackery Smith"
__email__ = "zackery.smith82307@gmail.com"
__copyright__ = "Copyright © 2020 Zackery Smith. All rights reserved."
__license__ = "GNU GPL-3.0"
__version_info__ = (0, 0, 1)
__version__ = ".".join(map(str, __version_info__))

import sys
sys.path.append("../../")
from reter.reter import (
    indicator,
    Cursor,
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
# listBox
########################################

def listBox(cursor, choices, theme: Optional[dict]={"pady": 0, "bullet": None, "bulletSelection": ">", "bulletSpacing": " ", "selectionHighlight": indicator.color.formatting.reverse, "highlightBullet": False, "selectionTextColor": None, "textColor": None, "bulletColor": None, "bulletSelectionColor": indicator.color.fg.red}):
    """
    Creates selection list of objects.

    :rtype: String
    :return: Returns selection 
    """
    # Wow this looks complex, most of it is turnary operaters that allow you to create theming

    # Create "padx". It is a bit of a challenge to create so I left it out for now.
    
    # Create y padding (top)
    if theme["pady"] != 0 and theme["pady"] > 0:
        print("\n"*theme["pady"], end="", flush=True)

    cursor.changeVisibility(False)
    lines = len(choices)
    for index, option in enumerate(choices):
        # Make sure only the needed amount of lines are created (according to theme)
        if index==lines-1:
            print((("" if theme["bulletSpacing"] == None else theme["bulletSpacing"]) if theme["highlightBullet"] == True else (" "*len(theme["bulletSelection"]) if theme["bullet"] == None else theme["bullet"])) + ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"]) + ("" if theme["textColor"] == None else theme["textColor"]) + option, end='', flush=True)
        
        elif index!=lines:
            print((("" if theme["bulletSpacing"] == None else theme["bulletSpacing"]) if theme["highlightBullet"] == True else (" "*len(theme["bulletSelection"]) if theme["bullet"] == None else theme["bullet"])) + ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"]) + ("" if theme["textColor"] == None else theme["textColor"]) + option)
        
        elif index==lines:  # Really never used. Kept just incase a user goes beyond other checks
            print((("" if theme["bulletSpacing"] == None else theme["bulletSpacing"]) if theme["highlightBullet"] == True else (" " if theme["bullet"] == None else theme["bullet"])) + ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"]) + ("" if theme["textColor"] == None else theme["textColor"]) + option, end='', flush=True)
    
    # Realign cursor
    cursor.move(0, len(choices)-1)
    cursor.align("left")

    startingLine = 1
    currentLine = 1
    while True:
        stripped = choices[currentLine-1].rstrip()
        # Current selected line theming
        sys.stdout.write((("" if theme["selectionHighlight"] == None else theme["selectionHighlight"]) if theme["highlightBullet"] == True else "")+(" " if theme["bulletSelection"] == None else ("" if theme["bulletSelectionColor"] == None else theme["bulletSelectionColor"]) + theme["bulletSelection"]) + ("" if theme["bulletSelectionColor"] == None else indicator.color.formatting.eoc) + ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"]) + ("" if theme["selectionHighlight"] == None else theme["selectionHighlight"]) + ("" if theme["selectionTextColor"] == None else theme["selectionTextColor"]) + stripped + indicator.color.formatting.eoc)
        
        cursor.align("left")
        key = captureKey()
        if key == indicator.arrow.up:
            if currentLine-1 <= 0:  # Make sure current line and cursor don't move any further
                continue  
            elif currentLine==0:
                currentLine+=1
                cursor.move(0, -1)
                continue
            currentLine-=1
            # Reset selection highlight (According to theme)
            sys.stdout.write((indicator.color.formatting.eoc if theme["textColor"] == None else theme["textColor"]) + (" "*len(theme["bulletSelection"]) if theme["bullet"] == None else theme["bullet"]) + ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"]) + stripped + indicator.color.formatting.eoc)
            cursor.align("left")
            
            cursor.move(0, 1)
        elif key == indicator.arrow.down:
            if currentLine+1 >= len(choices)+1:  # Make sure current line and cursor don't move any further
                continue
            elif currentLine > len(choices):
                currentLine-=1
                cursor.move(0, 1)
                continue
            currentLine+=1
            # Reset selection highlight (According to theme)
            sys.stdout.write((indicator.color.formatting.eoc if theme["textColor"] == None else theme["textColor"]) + (" "*len(theme["bulletSelection"]) if theme["bullet"] == None else theme["bullet"]) + ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"]) + stripped + indicator.color.formatting.eoc)
            cursor.align("left")
            
            cursor.move(0, -1)
        
        elif key == indicator.escape.enter:
            # Fix cursor (position, visibility, and add padding if needed)
            cursor.move(0, (len(choices)-currentLine)*-1)  # Fix pos
            if theme["pady"] != 0 and theme["pady"] > 0:
                print("\n"*theme["pady"], end="", flush=True)
                cursor.move(0, theme["pady"]*-1)
            cursor.changeVisibility(True)  # Fix visibility
            
            # Remove all special formating
            print(indicator.color.formatting.eoc, end="\n")

            return choices[currentLine-1]
        else:
            pass
