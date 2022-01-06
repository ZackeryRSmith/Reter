########################################
# IMPORT
########################################

from src.lib.style.colour import *
from src.lib.event.input.map.keys import *


########################################
# INDICATOR
########################################

class indicator:
    ###################
    # Parse
    ###################
    def parse(raw_character):
        """
        Parses a simple key output

        :param str raw_character: Char outputted by key press, E.g. "b'h'"
        """
        cleaned_char = str(raw_character).replace("b", "", 1).replace("'", "")
        parsed_char = ""
        if cleaned_char.startswith('\\') and cleaned_char[1] != '\\':  # Check for special char
            for item in keymap:
                if raw_character == item:
                    return keymap[item]
            print(cleaned_char)  # For debugging (Remove when all keys are mapped)
        else:
            parsed_char = cleaned_char
        return parsed_char
    

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


