# Delete File in Python

import os
if os.path.exists("file.txt"):
   os.remove("file.txt")
   print("The file has been deleted")
else:
    print("The file does not exist")