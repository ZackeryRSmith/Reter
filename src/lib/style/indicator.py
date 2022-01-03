# This code below should be put in a file called colour.py

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
# End of colour
EOC            = "\u001b[0m"



########################################
# INDICATOR
########################################

class indicator:
    def parse(rawCharacter):
        return str(rawCharacter).replace("b", "", 1).replace("'", "")


    class arrow:
        """
        Stores what an arrow means. This allows the end user to type `arrow.up` and let it be understood.
        """
        up = UPARROW
        down = DOWNARROW
        right = RIGHTARROW
        left = LEFTARROW
    

    class escape:
        """
        Store some extra escape chars. This allows the end user to type `arrow.up` and let it be understood
        """
        backspace = BACKSPACE
        enter = RETURN
        ctrl_d = FORMFEED
        xmit = XMIT
        etx = ETX
    

    class colour:
        class fg:
            # Black
            black = FGBLACK
            lightblack = FGLIGHTBLACK
            # Red
            red = FGRED 
            lightred = FGLIGHTRED 
            # Green
            green = FGGREEN  
            lightgreen = FGLIGHTGREEN 
            # Yellow
            yellow = FGYELLOW  
            lightyellow = FGLIGHTYELLOW 
            # Blue
            blue = FGBLUE    
            lightblue = FGLIGHTBLUE  
            # Magenta
            magenta = FGMAGENTA    
            lightmagenta = FGLIGHTMAGENTA 
            # Cyan
            cyan = FGCYAN
            lightcyan = FGLIGHTCYAN
            # White
            white = FGWHITE 
            lightwhite = FGLIGHTWHITE 
 

        class bg:
            # Black
            black = BGBLACK
            lightblack = BGLIGHTBLACK 
            # Red
            red = BGRED  
            lightred = BGLIGHTRED
            # Green
            green = BGGREEN  
            lightgreen = BGLIGHTGREEN 
            # Yellow
            yellow = BGYELLOW  
            lightyellow = BGLIGHTYELLOW 
            # Blue
            blue = BGBLUE 
            lightblue = BGLIGHTBLUE 
            # Magenta
            magenta = BGMAGENTA
            lightmagenta = BGLIGHTMAGENTA
            # Cyan
            cyan = BGCYAN  
            lightcyan = BGLIGHTCYAN  
            # White
            white = BGWHITE  
            lightwhite = BGLIGHTWHITE 
        

        class formatting:
            # Bold
            bold = BOLD
            # Underline
            underline = UNDERLINE
            # Reverse (Not text! Reverses the BG Colour!)
            reverse = REVERSED                          
            # End of colour
            eoc = EOC

