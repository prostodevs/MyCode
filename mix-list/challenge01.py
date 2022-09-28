#!/usr/bin/env python3

# create a list
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# print the list for the user
print(f"The full list is: {iplist}")

# print just the IP from the list
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")
