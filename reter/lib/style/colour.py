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

## Special formatting
###################################################################
#               Escape codes and names yoinked from,              #
#  https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797  #
#-----------------------------------------------------------------#
# Bold
BOLD           = "\u001b[1m"
# Dim
DIM            = "\u001b[2m"
# Italic
ITALIC         = "\u001b[3m"
# Underline
UNDERLINE      = "\u001b[4m"
# Blink (Blink text, how fun!)
BLINK          = "\u001b[5m"
# Reverse (Not text! Reverses the BG Colour!)
REVERSED       = "\u001b[7m"
# Hide (*poof*, magic)
HIDE           = "\u001b[8m"
# Strikethrough (W̶h̶o̶ ̶w̶o̶u̶l̶d̶ ̶e̶v̶e̶r̶ ̶n̶e̶e̶d̶ ̶s̶t̶r̶i̶k̶e̶t̶h̶r̶o̶u̶g̶h̶)
STRIKETHROUGH  = "\u001b[9m"
# End of colour
EOC            = "\u001b[0m"
#-----------------------------------------------------------------#


## Colour (256 fg, 256 bg). !! NOT TRUE COLOUR !!
def id_to_256(colour_id, layer):
    """
    Gives back the colour calculated using an id (Range: 0-255).

    :param int colour_id: A value between 0 and 255, 0 being the darkest while 256 being the lightest. If 255 limit is exceeded a NoneType will be returned.
    :param int layer: 0 being background (BG) while 1 being foreground (FG).

    :rtype: bytes
    :return: Returns a ANSI ESC code that when echoed, will tell the terminal to use said colour.
    """
    # Make sure colour_id and layer range is not exceeded
    if colour_id > 255 or colour_id < 0 or layer > 1 or layer < 0:
        # A range limit has been broken
        return None
    else:
        if layer == 0:
            # BG
            return bytes(f'\x1b[48;5;{colour_id}m', 'utf-8')
        else:
            # FG
            return bytes(f'\x1b[38;5;{colour_id}m', 'utf-8')



## True Colour
def rgb_to_ansi(red, green, blue, layer):
    """
    Gives back the colour calculated using RGB values

    :param int red: Amount of red in the colour
    :param int green: Amount of green in the colour
    :param int blue: Amount of blue in the colour
    
    :rtype: bytes
    :return: Returns a ANSI ESC code that when echoed will tell the terminal to use said colour
    """
    if layer > 1 or layer < 0:
        # Range limit has been broken
        return None
    else:
        if layer == 0:
            # BG
            return bytes(f'\x1b[48;2;{red};{green};{blue}m', 'utf-8')
        else:
            # FG
            return bytes(f'\x1b[38;2;{red};{green};{blue}m', 'utf-8')
