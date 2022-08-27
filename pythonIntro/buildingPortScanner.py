#!/bin/python3
# Building a port scanner

import sys
import socket
from datetime import datetime
import editme as em # is a custom module, look for editme.py in same dir.

# usage command: python3 buildingPortScanner.py <ip-address>

#define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPV4
else:
	print("Invalid amount of aurgments.")
	print("Syntax: python3 buildingPortScanner.py <ip>")

# adding a banner
em.nl()
print("*" *50)
print("Time started: " + str(datetime.now()))
print("Scanning target " + target + "...")
print("*" *50)

# Port scanner

try:
	for port in range(50,81):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		if result == 0:
			print("Port {} is open".format(port))
			em.nl()
			s.close()

except KeyboardInterrupt:
	em.nl()
	print("Exiting Program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.close()

except socket.error:
	print("Couldn't connect to server.")
	sys.close()

