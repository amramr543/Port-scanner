#!/bin/python3
import os
import sys
import socket
from datetime import datetime

hostname = sys.argv[1]

response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print(f"The host you give is : {hostname} is up!")
else:
  print(f"The host you give is : {hostname} is down!")
  exit()

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py")

#Add a pretty banner
print("-" * 50)
print("Scanning target "+hostname)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((hostname,port)) #returns an error indicator - if port is open it throws a 0, otherwise 1
		if result == 0:
			print(f"Port {port} is open")
		elif result == 1:
			print(" no ports open")
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit()