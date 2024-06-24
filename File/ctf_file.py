import os
import re
import subprocess
from pathlib import Path
import shutil

import zipfile
import tarfile

def fileIsValid(address):
    my_file = Path(address)

    if my_file.is_file():
        print("File Exist...")
        return True
    else:
        print("File not found...")
        return False

def initialize(address, flagID):
    if fileIsValid(address):
        readFileData(address, flagID)



def readFileData(address, flagID):
    print("File Command:")
    print(subprocess.run(["file", address], capture_output=True, text=True).stdout)

    print("")
    print("Strings Command:")
    file_strings = subprocess.run(["strings", address], capture_output=True, text=True).stdout
    print(re.findall(flagID+"\{[^}]*\}",file_strings, re.DOTALL))

    if(zipfile.is_zipfile(address)):
        path = os.path.dirname(os.path.realpath(address))
        with zipfile.ZipFile(address, "r") as zip_ref:
            zip_ref.extractall(path+"/extracted")
        
        for newAddress in os.listdir(path+"/extracted"):
            initialize(newAddress, flagID)
        
        shutil.rmtree(path+"/extracted")

