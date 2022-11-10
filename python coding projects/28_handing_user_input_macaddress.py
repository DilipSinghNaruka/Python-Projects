#!/usr/bin/env python
import subprocess
interface = raw_input("Type interface name > ")
new_mac = raw_input("type new mac address >")

print("[+] changing mac address for" + interface +"to" +new_mac) 

subprocess.call("ifconfg"+ interface + "down", shell=True)
subprocess.call("ifconfig" + interface + "hw ether" + new_mac , shell=True)
subprocess.call("ifcofig" + interface + "up", shell=True)

subprocess.call(["ifconfg"+ interface + "down"])
subprocess.call(["ifconfig" + interface + "hw ether" + new_mac ])
subprocess.call(["ifcofig" + interface + "up"])

#This not for windows 