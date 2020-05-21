#!/usr/bin/env python
# -*- coding: utf_8 -*-

"""
    Make a list of all the files and directories within the current directory,
    recursively.
"""

import os

###############################################################################
def main():
   """Script entry point."""
   for aRoot, aDirectories, aFiles in os.walk("."):
      print("Directory '%s'" % aRoot)
      for aFile in aFiles:
         print("File '%s/%s'" % (aRoot, aFile))

if __name__ == "__main__":
   main()
