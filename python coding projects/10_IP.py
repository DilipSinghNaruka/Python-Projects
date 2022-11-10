#socket give us information about network 

import socket

hostname = socket.gethostname()     #gethostname is showing hostname of this Pc

ip_address = socket.gethostbyname(hostname)#gethostnamebyid is showing IP of this Pc

print(f"Hostname: {hostname}")

print(f"IP Address: {ip_address}")

