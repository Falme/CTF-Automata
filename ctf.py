import sys
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re


print("==============================")
print("==== Falme's CTF Automata ====")
print("==============================\n")
print("Starting Application...\n\n")

if (len(sys.argv) <= 2):
    print("ERROR: Not Enough Arguments for the operation\n")
    print("Usage:")
    print("ctf.py <HttpAddress> <flagID>")
else:
    print("Looking for flags in address...")

    url = sys.argv[1]
    flagID = sys.argv[2]

    driver = webdriver.Firefox()
    
    driver.get(url)
    time.sleep(2)
    
    content = driver.page_source
    print("Flags Found in Page Source:")
    print(re.findall(flagID+"\{[^}]*\}",content, re.DOTALL))

    driver.close()
