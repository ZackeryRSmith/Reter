########################################
# IMPORTS
########################################

import sys
import os
from contextlib import contextmanager 


# https://stackoverflow.com/questions/4675728/redirect-stdout-to-a-file-in-python
########################################
# FILENO
########################################

def fileno(file_or_fd):
    fd = getattr(file_or_fd, 'fileno', lambda: file_or_fd)()
    if not isinstance(fd, int):
        raise ValueError("Expected a file (`.fileno()`) or a file descriptor")
    return fd


########################################
# STDOUT REDIRECT
########################################

def redirect():
    

sys.stdout = 

