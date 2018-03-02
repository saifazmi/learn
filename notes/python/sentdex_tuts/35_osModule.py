# OS module, part of standard library

import os

# Gets the current working directory
curDir= os.getcwd()
print(curDir)

# Makes a new directory in current directory
os.mkdir("newDir")

import time

# Time delay
time.sleep(3)

# Renames the newly created directory
os.rename("newDir", "newDir2")
time.sleep(3)

# Deletes the renamed directory
os.rmdir("newDir2")
