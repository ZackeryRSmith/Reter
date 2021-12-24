# Simple script that prints back key pressed
import sys
sys.path.append('../')
from reter.reter import captureKey

while True:
    print(captureKey())
