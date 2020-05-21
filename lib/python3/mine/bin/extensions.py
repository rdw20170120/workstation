#!/usr/bin/env python
# -*- coding: utf_8 -*-

"""
   Count the file extensions within the current directory, recursively.
   Ignore source control subdirectories (CVS, Mercurial, & Subversion)
"""

import os
import re

def prune(theDirectories, theFiles):
   remove(theDirectories, r".hg")
   remove(theDirectories, r".svn")
   remove(theDirectories, r"CVS")

def remove(theList, thePattern):
   for aValue in theList:
      if re.match(thePattern, aValue):
         theList.remove(aValue)

###############################################################################
def main():
   """Script entry point."""
   aCounts = {}
   for aRoot, aDirectories, aFiles in os.walk("."):
      prune(aDirectories, aFiles)
      # print "Directory '%s'" % aRoot
      for aFile in aFiles:
         # print "File '%s'" % aFile
         aPrefix, aExtension = os.path.splitext(aFile)
         if aExtension in aCounts:
            aCounts[aExtension] += 1
         else:
            aCounts[aExtension] = 1
   for aExtension in sorted(aCounts.keys()):
      print "%6u  %s" %(aCounts[aExtension], aExtension)

if __name__ == "__main__":
   main()
