import sys
sys.path.append('../')
from handle import Error


########################################
# ILLEGAL ARGUMENT ERROR
########################################

class IllegalArgumentError(Error):
    """Called when a argument unbeknown to us gets passed"""
    pass
