import sys
import tty
import termios
import os

# Get character
class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()  # Check if output medium is a terminal
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())  # Set file descripter (In this case terminal) to raw
            ch = sys.stdin.buffer.raw.read(3)  # Reads 3 chars
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # Set the tty attributes for file descriptor
        return ch

varList = ["Hello", "World", "Peekaboo"]
varValues = [15, 0, -18.3]
varIndex = 0

def updateInfo():
    global varList
    global varValues
    global varIndex
    if varIndex > len(varList)-1:
        varIndex -= len(varList)
    elif varIndex < 0:
        varIndex += len(varList)
    os.system("clear")
    print("""
          %s
          %s

            %s
""" % (varList[varIndex], varValues[varIndex], varIndex+1))

def get():
    ## Issue 1 (FIXED)
    # Letters only get registered after three presses.
    #
    # I beleave this has something to do with tty.setraw(). Unlike with the escape chars letters, numbers and etc
    # don't escape immediately, but after three inputs it auto escapes.
    #
    # Reading input as binary solved this issue along with other io issues. The three read presses issue is due to .read(3).
    # It will read 3 letters numbers whatever, escape chars like ^[[A are three (^[ counts as one char). The reason ^C (EXT)
    # would not work is it's under 3 chars (2 chars) meaning it would take to presses. I am not too sure why reading raw works
    # I have theories though.

    global varIndex
    global varValues
    keyPressed = _Getch()
    while True:
        k = keyPressed()
        if k != '':
            break
    if k==b'\x1b[A':  # Up
        varValues[varIndex] += 1
    elif k==b'\x1b[B':  # Down
        varValues[varIndex] -= 1
    elif k==b'\x1b[C':  # Right
        varIndex += 1
    elif k==b'\x1b[D':  # Left
        varIndex -= 1
    elif k==b'\x03':  # ETX
        # Switching up .read() to a binary form fixed this issue. Why... well who knows, but it works!
        raise KeyboardInterrupt("ctrl+c was pressed")
    else:
        # If it's not a key we are looking for we really do not care
        pass
    updateInfo()    

def main():
    while True:
        get()

if __name__=='__main__':
    main()
