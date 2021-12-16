""" Issue 3 (Enhancement)
Issue: It would be nice to have a "prefab" system where actions of things can be set. Lets say if I hit a char limit in captureInput(), instead
of breaking and stopping there you would be able to add code where it just blocks you from typing more. I can't really think of a good way to
implement something like this.
"""

########################################
# IMPORTS
########################################

import sys
import tty
import termios
import os
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
import subprocess


########################################
# CONSTANTS
########################################

# Aa
aKEY       = (b'a')
AKEY       = (b'A')
# Bb
bKEY       = (b'b')
BKEY       = (b'B')
# Cc
cKEY       = (b'c')
CKEY       = (b'C')
# Dd
dKEY       = (b'd')
DKEY       = (b'D')
# Ee
eKEY       = (b'e')
EKEY       = (b'E')
# Ff
fKEY       = (b'f')
FKEY       = (b'F')
# Gg
gKEY       = (b'g')
GKEY       = (b'G')
# Hh
hKEY       = (b'h')
HKEY       = (b'H') 
# Ii
iKEY       = (b'i')
IKEY       = (b'I')
# Jj
jKEY       = (b'j')
JKEY       = (b'J')
# Kk
kKEY       = (b'k')
KKEY       = (b'K')
# Ll
lKEY       = (b'l')
LKEY       = (b'L')
# Mm
mKEY       = (b'm')
MKEY       = (b'M')
# Nn
nKEY       = (b'n')
NKEY       = (b'N')
# Oo
oKEY       = (b'o')
OKEY       = (b'O')
# Pp
pKEY       = (b'p')
PKEY       = (b'P')
# Qq
qKEY       = (b'q')
QKEY       = (b'Q')
# Rr
rKEY       = (b'r')
RKEY       = (b'R')
# Ss
sKEY       = (b's')
SKEY       = (b'S')
# Tt
tKEY       = (b't')
TKEY       = (b'T')
# Uu
uKEY       = (b'u')
UKEY       = (b'U')
# Vv
vKEY       = (b'v')
VKEY       = (b'V')
# Ww
wKEY       = (b'w')
WKEY       = (b'W')
# Xx
xKEY       = (b'x')
XKEY       = (b'X')
# Yy
yKEY       = (b'y')
YKEY       = (b'Y')
# Zz
zKEY       = (b'z')
ZKEY       = (b'Z')

# Number keys
ONEKEY     = (b'1')
TWOKEY     = (b'2')
THREEKEY   = (b'3')
FOURKEY    = (b'4')
FIVEKEY    = (b'5')
SIXKEY     = (b'6')
SEVENKEY   = (b'7')
EIGHTKEY   = (b'8')
NINEKEY    = (b'9')
ZEROKEY    = (b'0')

# Function keys
F1         = (b'^[OP')
F2         = (b'^[OQ')
F3         = (b'^[OR')
F4         = (b'^[OS')
F5         = (b'^[[15~')
F6         = (b'^[[17~')
F7         = (b'^[[18~')
F8         = (b'^[[19~')
F9         = (b'^[[20~')
F10        = (b'^[[21~')
F11        = (b'^[[23~')
F12        = (b'^[[24~')

UPARROW    = (b'\x1b[A')
DOWNARROW  = (b'\x1b[B')
RIGHTARROW = (b'\x1b[C')
LEFTARROW  = (b'\x1b[D')
BACKSPACE  = (b'\x7f')  # backspace/delete 
RETURN     = (b'\r')  # return/enter
FORMFEED   = (b'\x0c')  # ctrl+l
XMIT       = (b'\x04')  # ctrl+d
ETX        = (b'\x03')  # ctrl+c

## Colours (16 basic fg, 16 basic bg)
# Black
FGBLACK        = "\u001b[30m"
FGLIGHTBLACK   = "\u001b[30;1m"
BGBLACK        = "\u001b[40m"
BGLIGHTBLACK   = "\u001b[40;1m"
# Red
FGRED          = "\u001b[31m"
FGLIGHTRED     = "\u001b[31;1m"
BGRED          = "\u001b[41m"
BGLIGHTRED     = "\u001b[41;1m"
# Green
FGGREEN        = "\u001b[32m"
FGLIGHTGREEN   = "\u001b[32;1m"
BGGREEN        = "\u001b[42m"
BGLIGHTGREEN   = "\u001b[42;1m"
# Yellow
FGYELLOW       = "\u001b[33m"
FGLIGHTYELLOW  = "\u001b[33;1m"
BGYELLOW       = "\u001b[43m"
BGLIGHTYELLOW  = "\u001b[43;1m"
# Blue
FGBLUE         = "\u001b[34m"
FGLIGHTBLUE    = "\u001b[34;1m"
BGBLUE         = "\u001b[44m"
BGLIGHTBLUE    = "\u001b[44;1m"
# Magenta
FGMAGENTA      = "\u001b[35m"
FGLIGHTMAGENTA = "\u001b[35;1m"
BGMAGENTA      = "\u001b[45m"
BGLIGHTMAGENTA = "\u001b[45;1m"
# Cyan
FGCYAN         = "\u001b[36m"
FGLIGHTCYAN    = "\u001b[36;1m"
BGCYAN         = "\u001b[46m"
BGLIGHTCYAN    = "\u001b[46;1m"
# White
FGWHITE        = "\u001b[37m"
FGLIGHTWHITE   = "\u001b[37;1m"
BGWHITE        = "\u001b[47m"
BGLIGHTWHITE   = "\u001b[47;1m"
# Bold
BOLD           = "\u001b[1m"
# Underline
UNDERLINE      = "\u001b[4m"
# Reverse (Not text! Reverses the BG Colour!)
REVERSED       = "\u001b[7m"                                
# End of color
EOC            = "\u001b[0m"



########################################
# ERRORS
########################################

class Error(Exception):  # Not currently being used but I see needs for this in the future.
    """Base class for other exceptions"""
    pass


########################################
# INDICATOR
########################################

class indicator:
    def parse(rawCharacter):
        return str(rawCharacter).replace("b", "", 1).replace("'", "")

    class letter:
        """ Issue 2 (ENHANCEMENT)
        Issue: There is most likely a better way to do this. I would like to not have this in the first place (I will create a function
        that makes this redundant). It's kinda hard to to have this though, nobody want to do `if key==b'a'` to check if the key pressed is
        equal to "a".
        """
        # Aa
        a = aKEY
        A = AKEY
        # Bb
        b = bKEY
        B = BKEY
        # Cc
        c = cKEY
        C = CKEY
        # Dd
        d = dKEY
        D = DKEY
        # Ee
        e = eKEY
        E = EKEY
        # Ff
        f = fKEY
        F = FKEY
        # Gg
        g = gKEY
        G = GKEY
        # Hh
        h = hKEY
        H = HKEY
        # Ii
        i = iKEY
        I = IKEY
        # Jj
        j = jKEY
        J = JKEY
        # Kk
        k = kKEY
        K = KKEY
        # Ll
        l = lKEY
        L = LKEY
        # Mm
        m = mKEY
        M = MKEY
        # Nn
        n = nKEY
        N = NKEY
        # Oo
        o = oKEY
        O = OKEY
        # Pp
        p = pKEY
        P = PKEY
        # Qq
        q = qKEY
        Q = QKEY
        # Rr
        r = rKEY
        R = RKEY
        # Ss
        s = sKEY
        S = SKEY
        # Tt
        t = tKEY
        T = TKEY
        # Uu
        u = uKEY
        U = UKEY
        # Vv
        v = vKEY
        V = VKEY
        # Ww
        w = wKEY
        W = WKEY
        # Xx
        x = xKEY
        X = XKEY
        # Yy
        y = yKEY
        Y = YKEY
        # Zz
        z = zKEY
        Z = ZKEY
    
    class number:
        """
        Stores what a number means. This allows the end user to type `number.one` and let it be understood.
        """
        one = ONEKEY
        two = TWOKEY
        three = THREEKEY
        four = FOURKEY
        five = FIVEKEY
        six = SIXKEY
        seven = SEVENKEY
        eight = EIGHTKEY
        nine = NINEKEY
        zero = ZEROKEY

    class arrow:
        """
        Stores what an arrow means. This allows the end user to type `arrow.up` and let it be understood.
        """
        up = UPARROW
        down = DOWNARROW
        right = RIGHTARROW
        left = LEFTARROW


########################################
# GETCH
########################################

class Getch:
    """
    Getch (Get character) will grab an input from the user. Taking in 3 characters max! This limit must be satisfied in one button press, this
    allows capturing of single key presses and escape character under 3 characters I.e. ^C
    """
    def __call__(self):
        """
        :rtype: class bytes
        :return: Returns character(s) pressed
        """
        fd = sys.stdin.fileno()  # Check if output medium is a terminal
        settings = termios.tcgetattr(fd)  # Gets file descripter attributes
        try:
            tty.setraw(sys.stdin.fileno())  # Set file descripter (In this case terminal) to raw
            ch = sys.stdin.buffer.raw.read(3)  # Reads 3 chars
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, settings)  # Set the tty attributes for file descriptor
        
        # This is not needed. It's here to make 100% sure a quit failsafe is implemented.
        if ch == ETX:
            raise KeyboardInterrupt("Default failsafe (ctrl+c)")
        return ch


########################################
# CURSOR
########################################
""" Issue 1 (Enhancement)
Issue: move() is the issue. I would like to make it more smart and just created the needed amount of lines. This would not be too hard to add
but in some cases it could get messy. I would like to make this modular/more configrable, I could do this by adding a sorta "theme" system. Man 
created things and such, the themes may not really apply to move() but I would like to add a theming system to reter.
"""

class Cursor:
    """
    Terminal cursor.
    """
    def __init__(self, posx, posy, visibility: Optional[bool]=True):
        """ 
        Constructor to initialize the object
        
        :param int posx: Begining x position for cursor
        :param int posy: Begining y position for cursor
        :param bool visibility: True = Shown, False = Hidden
        """
        self.posx = posx
        self.posy = posy
        self.visibility = visibility
        if self.visibility:
            sys.stdout.write("\x1b[?25h")
        else:
            sys.stdout.write("\x1b[?25l")


    def changeVisibility(self, visibility):
        """
        Changes the visibility of cursor

        :param bool visibility: True = Shown, False = Hidden
        """
        self.visibility = visibility
        if self.visibility:
            sys.stdout.write("\x1b[?25h")
        else:
            sys.stdout.write("\x1b[?25l")


    def getPos(self):
        # Broken who knows why
        # \x1b[6n
        pass        


    def setPos(self, x, y):
        """
        Sets the position of cursor. If you are looking for changing the value and not setting the value look towards .move().

        :param int x: x position to set
        :param int y: y position to set
        """
        self.posx = x
        self.posy = y
        sys.stdout.write('\033[%s;%sH' % (self.posx, self.posy))        


    def move(self, x, y):
        """
        Changes the position of the cursor. If you are looking to set the value and not change the value look towards .setPos().

        :param int x: x position to change
        :param int y: y position to change
        """
        self.posx = x
        self.posy = y
        if self.posx > 0:
            sys.stdout.write('\x1b[%sC' % (self.posx))
        elif self.posx < 0:
            sys.stdout.write('\x1b[%sD' % (int(str(self.posx)[1:])))  # Removes negative number with splicing
        
        if self.posy > 0:
            sys.stdout.write('\x1b[%sA' % (self.posy))
        elif self.posy < 0:
            sys.stdout.write('\x1b[%sB' % (int(str(self.posy)[1:])))  # Removes negative number with splicing
        sys.stdout.flush()  # Update line


    def align(self, position):
        """
        Align cursor position with preset position E.g. "left" will put the cursor to the left side. "tright" will place the cursor in the
        top right of the screen

        :param string position: The position to go to I.e. 
                                           "tleft" "tmiddle" "tright"
                                            "left" "middle" "right"
                                           "bleft" "bmiddle" "bright"
        """
        if position=="left":
            self.move(-100, 0)
        elif position=="right":
            self.move(100, 0)


""" Yeah... there is a better way to do this
########################################
# LINE
########################################

class Line:
    def get():
        sys.stdout.write("\x1b[6n")

    def highlight(smartHighlight=True, starPos: Optional[int]=0, endPos: Optional[int]=0):
        if smartHighlight:
            print("Test")
"""


########################################
# CAPTURE KEY
########################################

def captureKey():
    """
    captureKey just takes Getch() and makes it usable by an end user.
    
    :rtype: class bytes
    :return: Returns key press
    """
    keyPressed = Getch()
    while True:
        key = keyPressed()
        if key != '':
            break
    if key==ETX:
        raise KeyboardInterrupt("Default failsafe (ctrl+c)")
    return key


########################################
# CAPTURE INPUT
########################################

def captureInput(blind: Optional[bool]=False, limit: Optional[int]=9223372036854775807):
    """
    captureInput will take the users key presses until a specified length is hit or enter key is pressed
    
    :param bool blind: If true input will not be shown when typing. Default is false
    :param int limit: You may set a limit to the number of characters that can be used. Good for passwords and such. Default is 9223372036854775807
    :rtype: String
    :return: Returns a string (String is used to ignore escape characters and ANSI in general.. also maybe because it makes my life easy...)
    """
    stringToReturn = ""
    cursor = Cursor(0, 0)
    while True:
        # Make sure limit if supplied is met
        if len(stringToReturn) >= limit:
            break # Making a more customizable system would be nice
        key = captureKey()
        if key == RIGHTARROW:
            cursor.move(1, 0)
            continue
        elif key == LEFTARROW:
            cursor.move(-1, 0)
            continue
        elif key == UPARROW:
            continue
        elif key == DOWNARROW:
            continue
        elif key == BACKSPACE:
            stringToReturn = stringToReturn[0:-1]  # Remove character from final return string
            sys.stdout.write("\b")  # Backup a character
            sys.stdout.write(" ")  # Replace character with blankspace
            sys.stdout.write("\b")  # Move back the cursor again.
            sys.stdout.flush()  # Refresh line
            continue  # Loop back the while loop (Stops the program from registering backspace escape code)
        elif key == RETURN:
            break
        if blind:
            stringToReturn+=str(key).replace("b", "", 1).replace("'", "")
        else:
            sys.stdout.write(str(key).replace("b", "", 1).replace("'", ""))
            sys.stdout.flush()
            stringToReturn+=str(key).replace("b", "", 1).replace("'", "")
    
    print("", end="\n")  # Fixes next print printing on same line.
    return stringToReturn


########################################
# listBox
########################################

def listBox(cursor, choices):
    """
    """
    cursor.changeVisibility(False)
    lines = len(choices)
    for index, option in enumerate(choices):
        # Make sure only the needed amount of lines are created
        if index==lines-1:
            print(option, end='', flush=True)
        elif index!=lines:
            print(option)
        elif index==lines:
            print(option, end='', flush=True)
    # Realign cursor
    cursor.move(0, len(choices)-1)
    cursor.align("left")

    startingLine = 1
    currentLine = 1
    while True:
        stripped = choices[currentLine-1].rstrip()
        sys.stdout.write(REVERSED + stripped + EOC)
        cursor.align("left")
        key = captureKey()
        if key == UPARROW:
            if currentLine-1 <= 0:  # Make sure current line and cursor don't move any further
                continue  
            elif currentLine==0:
                currentLine+=1
                cursor.move(0, -1)
                continue
            currentLine-=1
            # Reset selection highlight
            sys.stdout.write(EOC + stripped + EOC)
            cursor.align("left")
            
            cursor.move(0, 1)
        elif key == DOWNARROW:
            if currentLine+1 >= len(choices)+1:  # Make sure current line and cursor don't move any further
                continue
            elif currentLine > len(choices):
                currentLine-=1
                cursor.move(0, 1)
                continue
            currentLine+=1
            # Reset selection highlight
            sys.stdout.write(EOC + stripped + EOC)
            cursor.align("left")
            
            cursor.move(0, -1)
        else:
            pass


########################################
# MAIN - FOR DEBUGGING REASONS
########################################

def main():
    cursor = Cursor(0, 0)
    #print(cursor.getPos())
    listBox(cursor, ["Hello", "World", "Green", "Eggs"])
    """ ANSI cursor movement test
    while True:
        key = captureKey()
        if key == LEFTARROW:
            cursor.move(-1, 0)
        elif key == RIGHTARROW:
            cursor.move(1, 0)
        elif key == UPARROW:
            cursor.move(0, 1)
        elif key == DOWNARROW:
            cursor.move(0, -1)
        else:
            pass
    """

########################################
# RUN - FOR DEBUGGING REASONS
########################################

if __name__=='__main__':
    main()


