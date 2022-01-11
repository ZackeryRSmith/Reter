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

from lib.terminal.term import Terminal 
from lib.terminal.screen import Screen, Line
from lib.event.input.keyboard.keyboard import Keyboard
from lib.style.indicator import indicator
from lib.style.colour import rgb_to_ansi, id_to_256
from lib.errhandler.handle import *
from lib.cursor.cursor import Cursor


########################################
# MAIN - FOR DEBUGGING REASONS
########################################

def main():
    from lib.terminal.term import Terminal 
    from lib.terminal.screen import Screen, Line
    from lib.event.input.keyboard.keyboard import Keyboard
    from lib.style.indicator import indicator
    from lib.style.colour import rgb_to_ansi, id_to_256
    from lib.cursor.cursor import Cursor


########################################
# RUN - FOR DEBUGGING REASONS
########################################

if __name__=='__main__':
    main()


