import reter

# Example of using Getch
"""
while True:
    keyPressed = reter.Getch()
    while True:
        key = keyPressed()
        if key != '':
            break
    if key==reter.ETX:
        raise KeyboardInterrupt("Default failsafe (ctrl+c)")
    print(key)
"""

# Example of using captureKey
"""
while True:
    print(reter.captureKey())
"""

# Example of parsing captureKey automatically I.e takes some thing like b'a' to "a"
while True:
    print(reter.indicator.parse(reter.captureKey()))
