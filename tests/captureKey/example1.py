import sys
sys.path.append('../')
from reter.reter import (
    indicator, 
    captureKey, 
    Getch, 
    ETX
)

# Example of using Getch
"""
while True:
    keyPressed = Getch()
    while True:
        key = keyPressed()
        if key != '':
            break
    if key==ETX:
        raise KeyboardInterrupt("Default failsafe (ctrl+c)")
    print(key)
"""

# Example of using captureKey
"""
while True:
    print(captureKey())
"""

# Example of parsing captureKey automatically I.e takes some thing like b'a' to "a"
while True:
    print(indicator.parse(captureKey()))
