########################################
# IMPORTS
########################################

import sys
from typing import Optional
from reter.lib.style.indicator import indicator


########################################
# CONSTANTS
########################################

FGRED = indicator.colour.fg.red
FGYELLOW = indicator.colour.fg.yellow
FGCYAN = indicator.colour.fg.cyan
EOC = indicator.colour.formatting.eoc


########################################
# ERROR
########################################

# Could be fixed up to look better. I will pretty much copy rust's error system...
class Error(Exception):
    """Base class for other exceptions"""
    def __init__(self, errorName, codeInQuestion, fixes: Optional[str]=None, info: Optional[str]=None):
        """Constructor to initialize object"""
        self.errorName = errorName
        self.codeInQuestion = codeInQuestion
        self.fixes = fixes
        self.info = info
        print(FGRED+"Oops.. it seems an issue has occurred:\n\n"+EOC+FGRED+self.errorName+FGYELLOW+"\n+-----------------------------------+"+EOC)
        print("""
%sCode in question
%s`
%s
`%s
%s------------------------------------+""" % (FGYELLOW, FGCYAN, self.codeInQuestion, EOC, FGYELLOW))
        if self.fixes != None:
            print("""
%sPotential fixes
%s`
%s
`%s
%s------------------------------------+""" % (FGYELLOW, FGCYAN, self.fixes, EOC, FGYELLOW))
        if self.info != None:
            print("""
%sAdditional info
%s`
%s
`%s""" % ((FGYELLOW, FGCYAN, self.info, EOC)))
        print("%s+-----------------------------------+%s" % (FGYELLOW, EOC))    

