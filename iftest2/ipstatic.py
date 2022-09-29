#!/usr/bin/env python3
""" Alta3 Research | J Stowe
    Fun with Conditionals """

def main():
    # prompt user for an address
    ipchk = input("192.168.0.1") 

    # a string tests as True
    if ipchk:
       print("Looks like the IP address was set: " + ipchk)
