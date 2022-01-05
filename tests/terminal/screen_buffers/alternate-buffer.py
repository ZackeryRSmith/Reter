# ::TODO::
# Create some way to edit the original buffer, while keeping the alternate buffer loaded.

# 1. Remove input of any kind during buffer (Loading screen system)  :: Done
# 2. Edit original buffer, while keeping alternate buffer active

import termios
import tty
import sys
import time


print("\033[?1049h\033[H")

old_settings = termios.tcgetattr(sys.stdin)
settings = termios.tcgetattr(sys.stdin)
settings[3] = settings[3] & ~(termios.ECHO | termios.ICANON)  # Disable echo, and stop the terminal from waiting for key press
termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, settings)
try:
    print("Alternate buffer!")
 
    for i in range(5, 0, -1):
        print("Going back in:", i)
        time.sleep(1)
 
finally:
    termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, old_settings)  # Re-enables "echo"
    print("\033[?1049l")  # Restore screen
