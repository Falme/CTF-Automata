from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

def initialize(address, flagID):
    print("Looking for flags in Address...")

    driver = webdriver.Firefox()
    
    driver.get(address)
    time.sleep(2)
    
    content = driver.page_source
    print("Flags Found in Page Source:")
    print(re.findall(flagID+"\{[^}]*\}",content, re.DOTALL))

    driver.close()