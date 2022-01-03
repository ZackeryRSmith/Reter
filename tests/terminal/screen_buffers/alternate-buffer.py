# ::TODO::
# Create some way to edit the original buffer, while keeping the alternate buffer loaded.

import time
 
print("\033[?1049h\033[H")
print("Alternate buffer!")
 
for i in range(5, 0, -1):
    print("Going back in:", i)
    time.sleep(1)
 
print("\033[?1049l")
