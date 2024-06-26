import sys
import validators

import Web.ctf_web as ctf_web
import File.ctf_file as ctf_file
import Tcp.ctf_tcp as ctf_tcp

print("==============================")
print("==== Falme's CTF Automata ====")
print("==============================\n")
print("Starting Application...\n\n")

if (len(sys.argv) <= 2):
    print("ERROR: Not Enough Arguments for the operation\n")
    print("Usage:")
    print("ctf.py <WebURLAddress or PathAddress> <flagID>")
    print("ctf.py <Tcp Address> <Port> <flagID>")
elif (len(sys.argv) <= 3):
    address = sys.argv[1]
    flagID = sys.argv[2]

    if validators.url(address):
        print("Address is an URL...")
        ctf_web.initialize(address, flagID)
    else:
        print("Address is not an URL...")
        print("Trying File in System...")
        print("")

        ctf_file.initialize(address, flagID)
else:
    print("Trying an Tcp connection...")

    address = sys.argv[1]
    port = sys.argv[2]
    flagID = sys.argv[3]

    ctf_tcp.initialize(address, port, flagID)

