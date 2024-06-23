import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import validators
import subprocess


print("==============================")
print("==== Falme's CTF Automata ====")
print("==============================\n")
print("Starting Application...\n\n")

if (len(sys.argv) <= 2):
    print("ERROR: Not Enough Arguments for the operation\n")
    print("Usage:")
    print("ctf.py <WebURLAddress or PathAddress> <flagID>")
else:

    address = sys.argv[1]
    flagID = sys.argv[2]

    validation = validators.url(address)

    if validation:
        print("Address is an URL...")
        print("Looking for flags in Address...")

        driver = webdriver.Firefox()
        
        driver.get(address)
        time.sleep(2)
        
        content = driver.page_source
        print("Flags Found in Page Source:")
        print(re.findall(flagID+"\{[^}]*\}",content, re.DOTALL))

        driver.close()
    else:
        print("Address is not an URL...")
        print("Trying File in System...")
        print("")

        print("File Command:")
        print(subprocess.run(["file", address], capture_output=True, text=True))

        print("")
        print("Strings Command:")
        file_strings = str(subprocess.run(["strings", address], capture_output=True, text=True))
        print(re.findall(flagID+"\{[^}]*\}",file_strings, re.DOTALL))


