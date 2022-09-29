#!/usr/bin/env python3

import shutil
import os

def main():
    # set 'default' directory
    os.chdir("/home/student/MyCode/")
    # 
    shutil.move("raynor.obj","ceph_storage/")

    # prompt user for a filename for kerrigan.obj
    xname = input("What is the new name for kerrigan.obj? ")
    
    # move the raynor.obj from MyCode to ceph_storage
    shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)

# import guard for main
if __name__ == "__main__":
    main()
