########################################
# IMPORT
########################################

from lib.style.colour import *
from lib.event.input.map.keys import *  


########################################
# INDICATOR
########################################

class indicator:
    ###################
    # Parse
    ###################
    def parse(rawCharacter):
        """
        Parses a simple key output

        :param str rawCharacter: Char outputted by key press, E.g. "b'h'"
        """
        # This code needs to be added upon, although functional 
        return str(rawCharacter).replace("b", "", 1).replace("'", "")

    
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
            # Underline
            underline = UNDERLINE
            # Reverse (Not text! Reverses the BG Colour!)
            reverse = REVERSED                          
            # End of colour
            eoc = EOC


