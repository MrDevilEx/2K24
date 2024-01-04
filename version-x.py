import os
import platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == "32bit":
    print(" Your Device is 32bit ")
    print(" Supported ✓ ")
    __import__("dev32")
elif bit == "64bit":
    print(" Your Device is 64bit ")
    print(" Supported ✓ ")
    __import__("dev64")
