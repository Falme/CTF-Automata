import re
import subprocess

def initialize(address, port, flagID):
    print("Looking for flags in Address...")

    content = subprocess.run(["nc", address, port], capture_output=True, text=True).stdout

    print(content)

    print("Flags Found in connection:")
    print(re.findall(flagID+"\{[^}]*\}",content, re.DOTALL))