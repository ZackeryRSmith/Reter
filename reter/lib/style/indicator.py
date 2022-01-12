########################################
# IMPORT
########################################

from reter.lib.style.colour import *
from reter.lib.event.input.map.keys import *
import re
import string
from typing import (
    AnyStr,
    Optional
)


########################################
# INDICATOR
########################################

class indicator:
    ###################
    # Parse
    ###################
    def parse(c: AnyStr, rt: Optional[bool]=False):
        """
        Parses a key output

        :param str c: Char outputted by key press, E.g. "b'h'" or "\x1b[A"
        :param bool rt: Regular Type, if True this will only output regular chars like "a", "b", or "c" not "\\x1b[1"
        """
        cleaned_char = str(c).replace("b", "", 1).replace("'", "")
        parsed_char = ""
        if cleaned_char.startswith('\\') and cleaned_char[1] != '\\':
            if rt == False:
                # Check for special char
                for item in keymap:
                    if c == item:
                        return keymap[item]
                print(cleaned_char)  # For debugging (Remove when all keys are mapped)
        else:
            parsed_char = cleaned_char
        return parsed_char
    

    ###################
    # Clean
    ###################
    def clean(s: AnyStr, esc: Optional[bytes]):
        """
        Cleans off string off all ANSI ESC codes. If the detection does not pick up the ESC code you may supply one your self.

        :param str s: String to be cleaned
        :param bytes esc: The ESC code to be cleaned (Optional, but you may supply it ONLY if it doesn't get auto detected)
        """
        if esc != None:
            return str(s).replace(esc.decode("utf-8"))
        else:
            return "".join(char for char in s if char not in string.printable)


    ###################
    # Byte to string
    ###################
    def byte_to_str(byte) -> str:
        """
        Byte to raw string
        """
        return byte.decode('utf-8')


    ########################################
    # ARROW - Parent: indicator
    ########################################
    
    class arrow:
        """
        Stores what an arrow means. This allows the end user to type `arrow.up` and let it be understood.
        """
        up = UPARROW
        down = DOWNARROW
        right = RIGHTARROW
        left = LEFTARROW
 

    ########################################
    # ESCAPE - Parent: indicator
    ########################################

    class escape:
        """
        Store some extra escape chars. This allows the end user to type `arrow.up` and let it be understood
        """
        backspace = BACKSPACE
        enter = RETURN
        ctrl_d = FORMFEED
        xmit = XMIT
        etx = ETX
    

    ########################################
    # COLOUR - Parent: indicator
    ########################################
    
    class colour:
        ########################################
        # FG - Parent: colour
        ########################################
        
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
 

        ########################################
        # BG - Parent: colour
        ########################################
        
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
        

        ########################################
        # FORMATTING - Parent: colour
        ########################################
        
        class formatting:
            # Bold
            bold = BOLD
            
            # Dim
            dim = DIM 
            # Italic
            italic = ITALIC         
            # Underline
            underline = UNDERLINE
            # Blink (Blinking text, how fun!)
            blink = BLINK
            # Reverse (Not text! Reverses the BG Colour!)
            reverse = REVERSED                          
            # Hide (*poof*, magic)
            hide = HIDE
            # Strikethrough (W̶h̶o̶ ̶w̶o̶u̶l̶d̶ ̶e̶v̶e̶r̶ ̶n̶e̶e̶d̶ ̶s̶t̶r̶i̶k̶e̶t̶h̶r̶o̶u̶g̶h̶)
            strikethrough = STRIKETHROUGH
            # End of colour
            eoc = EOC


