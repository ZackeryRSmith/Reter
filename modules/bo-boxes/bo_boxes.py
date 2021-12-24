#!/usr/bin/env python
###########################################################################     
#                                                                         #     
#                          Bo-Boxes (Wombo, combo!)                       #     
#                                      ~ Creating some nice boxes!        #     
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


import sys
sys.path.append("../../")
from reter.reter import (
    indicator,
    init,
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
#-- Small issues
# Lag on some terminals
# Cursor movement is just laggy when it comes to some terminals
# 'Some terminals' mainly refer to Terminator, and Gnome Terminal


def listBox(terminal, choices, cycleCursor: Optional[bool]=True, clearScreen: Optional[bool]=False, clearMenuOnExit: Optional[bool]=False, cursorIndex: Optional[int]=0, theme: Optional[dict]={"pady": 0, "bullet": None, "bulletSelection": ">", "bulletSpacing": " ", "selectionHighlight": indicator.colour.formatting.reverse, "highlightBullet": False, "selectionTextColor": None, "textColor": None, "bulletColor": None, "bulletSelectionColor": indicator.colour.fg.red}):
    """
    Creates selection list of objects.

    :rtype: String
    :return: Returns selection 
    """
    # Create "padx". It is a bit of a challenge to create so I left it out for now.
    
    # Fix up theme now, reduces the number of conditional checks. Thus speeding up are script, and making it look better!
    theme = {
        "pady": theme["pady"],
        "bullet": ("" if theme["bulletSelection"] == None else " "*len(theme["bulletSelection"])) if theme["bullet"] == None else theme["bullet"],
        "bulletSelection": " " if theme["bulletSelection"] == None else theme["bulletSelection"],
        "bulletSpacing": "" if theme["bulletSpacing"] == None else theme["bulletSpacing"],
        "selectionHighlight": "" if theme["selectionHighlight"] == None else theme["selectionHighlight"],
        "highlightBullet": "" if theme["highlightBullet"] == False else "" if theme["selectionHighlight"] == None else theme["selectionHighlight"],
        "selectionTextColor": "" if theme["selectionTextColor"] == None else theme["selectionTextColor"],
        "textColor": "" if theme["textColor"] == None else theme["textColor"],
        "bulletColor": "" if theme["bulletColor"] == None else theme["bulletColor"],
        "bulletSelectionColor": "" if theme["bulletSelectionColor"] == None else theme["bulletSelectionColor"]
    }

    # Create y padding (top)
    if theme["pady"] > 0:
        print("\n"*theme["pady"], end="", flush=True)

    terminal.cursor.changeVisibility(False)  # Hide cursor
    
    chunkedLines = []
    for index, item in enumerate(choices):
        print(theme["bullet"]+theme["bulletSpacing"]+item)  # Print entries in unselected form
        chunkedLines.append(terminal.line.chunkIt(terminal.screen, theme["bulletSpacing"], index+(len(choices)-1), 1))

    # Move cursor to first element
    terminal.cursor.move(0, -len(choices))
    initPos = terminal.cursor.getPos()

    # Set init selected line
    chunkedLines[initPos[1]-(len(choices)-1)][0].setColour(terminal.cursor, theme["bulletSelectionColor"])
    
    # Move cursor back to first element
    terminal.cursor.setPos(initPos[0], initPos[1])

    while True:
        key = captureKey()
        if key == indicator.arrow.up:
            if terminal.cursor.getPos("y") <= initPos[1]:
                if cycleCursor:
                    chunkedLines[int(terminal.cursor.posy)-(len(choices)-1)][0].setColour(terminal.cursor, fg=indicator.colour.formatting.eoc, bg=indicator.colour.formatting.eoc)
                    terminal.cursor.move(0, len(choices)-1)
                    chunkedLines[terminal.cursor.getPos("y")-(len(choices)-1)][0].setColour(terminal.cursor, theme["bulletSelectionColor"])
                else:
                    pass
            else:
                chunkedLines[int(terminal.cursor.posy)-(len(choices)-1)][0].setColour(terminal.cursor, fg=indicator.colour.formatting.eoc, bg=indicator.colour.formatting.eoc)
                terminal.cursor.move(0, -1)        
                chunkedLines[terminal.cursor.getPos("y")-(len(choices)-1)][0].setColour(terminal.cursor, theme["bulletSelectionColor"])
        
        elif key == indicator.arrow.down:
            if terminal.cursor.getPos("y") >= initPos[1]+(len(choices)-1):
                if cycleCursor:
                    chunkedLines[int(terminal.cursor.posy)-(len(choices)-1)][0].setColour(terminal.cursor, fg=indicator.colour.formatting.eoc, bg=indicator.colour.formatting.eoc)
                    terminal.cursor.move(0, -(len(choices)-1))
                    chunkedLines[terminal.cursor.getPos("y")-(len(choices)-1)][0].setColour(terminal.cursor, theme["bulletSelectionColor"])
                else:
                    pass
            else:
                chunkedLines[int(terminal.cursor.posy)-(len(choices)-1)][0].setColour(terminal.cursor, fg=indicator.colour.formatting.eoc, bg=indicator.colour.formatting.eoc)
                terminal.cursor.move(0, 1)
                chunkedLines[terminal.cursor.getPos("y")-(len(choices)-1)][0].setColour(terminal.cursor, theme["bulletSelectionColor"])

        elif key == indicator.escape.enter:
            selection = choices[terminal.cursor.getPos("y")-(len(choices)-1)]  # Save selected option
            terminal.cursor.setPos(0, terminal.cursor.getPos("y")+(len(choices)-choices.index(selection)))  # Move cursor past choices
            return selection  # Return selected option

    terminal.cursor.changeVisibility(True)  # Show cursor
    if clearScreen:
        terminal.screen.wipe()
    else:
        terminal.screen.cachedScreen = ""  # Clean cachedScreen
   

########################################
# MAIN - FOR DEBUGGING REASONS
########################################

def main():
    terminal = init()
    print("Select an entry!")
    print("%s Was selected" % (listBox(terminal, ["entry 1", "entry 2", "entry 3"])))


########################################
# RUN - FOR DEBUGGING REASONS
########################################

if __name__=='__main__':
    main()


