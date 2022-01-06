#!/usr/bin/env python
###########################################################################     
#                                                                         #     
#                          Reter (Retry Terminal)                         #     
#                                      ~ Lets try this again..            #     
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


########################################
# IMPORTS
########################################

from src.lib.terminal.terminal import Terminal
from src.lib.terminal.screen import Screen, Line
from src.lib.event.input.keyboard.keyboard import Keyboard
from src.lib.style.indicator import indicator
from src.lib.style.colour import rgb_to_ansi, id_to_256
from src.lib.errhandler.handle import *
from src.lib.cursor.cursor import Cursor
# Misc imports
import time


########################################
# MAIN - FOR DEBUGGING REASONS
########################################

def main():
    terminal = Terminal().quick_start()
    bts = indicator.byte_to_str  # Byte to string.. not the k-pop band
    EOC = indicator.colour.formatting.eoc  # End of color
    blink = indicator.colour.formatting.blink  # Blinking
    bold = indicator.colour.formatting.bold  # Bold 
    print(bts(rgb_to_ansi(255, 40, 53, 1))+blink+bold+"Hello, World!"+EOC)


########################################
# RUN - FOR DEBUGGING REASONS
########################################

if __name__=='__main__':
    main()


