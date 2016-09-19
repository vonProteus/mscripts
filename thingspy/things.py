#!/usr/bin/python

import sys, getopt, locale
import plistlib


from ToDo import ToDo
from Project import Project

class thingspy:
    def __init__(self):
        self.toAddFile = ""
        self.todos = []
        self.projects = []
        self.plist = []
        return

    def main(self, argv):
        self.parseParam(argv)
        self.plist = plistlib.readPlist(self.toAddFile)
        print(self.plist)



    def parseParam(self, args):
        try:
            opts, args = getopt.getopt(args,"ha:",["to-add="])
        except getopt.GetoptError:
            print sys.argv[0]+' -a <toAdd.plist>'
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print sys.argv[0]+' --to-add= <toAdd.plist>'
                sys.exit()
            elif opt in ("-a", "--to-add"):
                self.toAddFile = arg




if __name__ == "__main__":
    obj = thingspy();
    obj.main(sys.argv[1:])