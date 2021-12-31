########################################
# IMPORTS
########################################

from typing import Optional


# Requires style indicator
########################################
# ERROR
########################################

class Error(Exception):
    """Base class for other exceptions"""
    def __init__(self, errorName, codeInQuestion, fixes: Optional[str]=None, info: Optional[str]=None):
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

