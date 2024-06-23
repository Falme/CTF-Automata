import re
import subprocess
from pathlib import Path

def initialize(address, flagID):

    if fileIsValid(address):
        print("File Command:")
        print(subprocess.run(["file", address], capture_output=True, text=True))

        print("")
        print("Strings Command:")
        file_strings = str(subprocess.run(["strings", address], capture_output=True, text=True))
        print(re.findall(flagID+"\{[^}]*\}",file_strings, re.DOTALL))

def fileIsValid(address):
    my_file = Path(address)

    if my_file.is_file():
        print("File Exist...")
        return True
    else:
        print("File not found...")
        return False