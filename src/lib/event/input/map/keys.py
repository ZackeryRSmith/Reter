### Define keys, ANSI -> Python :: NOTE : Not 100% up-to-date with keymap dict
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


# ANSI -> English
keymap = {
    #############################################################
    #            Escape codes and names yoinked from,           #
    #  https://www.physics.udel.edu/~watson/scen103/ascii.html  #
    #-----------------------------------------------------------#
    b'\x01':"soh",          # ctrl+a | Start of Heading
    b'\x02':"stx",          # ctrl+b | Start of Text
    b'\x03':"etx",          # ctrl+c | End of Text
    b'\x04':"eot",          # ctrl+d | End of Xmit
    b'\x05':"enq",          # ctrl+e | Enquiry
    b'\x06':"ack",          # ctrl+f | Acknowledge
    b'\x07':"bel",          # ctrl+g | Bell
    b'\x08':"bs",           # ctrl+h | Backspace
    b'\t':"ht",             # ctrl+i | Horizontal Tab
    b'\n':"lf",             # ctrl+j | Line Feed
    b'\x0b':"vt",           # ctrl+k | Vertical Tab
    b'\x0c':"ff",           # ctrl+l | Form Feed
    b'\r':"cr",             # ctrl+m | Carriage Feed
    b'\x0e':"so",           # ctrl+n | Shift Out
    b'\x0f':"si",           # ctrl+o | Shift In
    b'\x10':"dle",          # ctrl+p | Data Line Escape
    b'\x11':"dc1",          # ctrl+q | Device Control 1
    b'\x12':"dc2",          # ctrl+r | Device Control 2
    b'\x13':"dc3",          # ctrl+s | Device Control 3
    b'\x14':"dc4",          # ctrl+t | Device Control 4
    b'\x15':"nak",          # ctrl+u | Neg Acknowledge
    b'\x16':"syn",          # ctrl+v | Synchronous Idel
    b'\x17':"etb",          # ctrl+w | End of Xmit Block 	
    b'\x18':"can",          # ctrl+x | Cancel
    b'\x19':"em",           # ctrl+y | End of Medium
    b'\x1a':"sub",          # ctrl+z | Substitute
    b'\x1b':"esc",          # ctrl+[ | Escape
    b'\x1c':"fs",           # ctrl+\ | File Separator
    b'\x1d':"gs",           # ctrl+] | Group Separator
    b'\x1e':"rs",           # ctrl+^ | Record Separator
    b'\x1f':"us",           # ctrl+_ | Unit Separator
    b'\x7f':"bs",           # delete | Backspace
    #-----------------------------------------------------------#
    b'\x1b[A':"uparrow", 
    b'\x1b[B':"downarrow", 
    b'\x1b[C':"rightarrow",
    b'\x1b[D':"leftarrow"}
