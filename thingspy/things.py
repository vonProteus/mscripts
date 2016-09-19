#!/usr/bin/python

import sys, getopt, locale
import plistlib
from subprocess import Popen, PIPE


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
        self.fillProjectsAndTodos()

        self.addToThings()


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

    def fillProjectsAndTodos(self):
        for pProject in self.plist["Projects"] :
            self.projects.append(Project(pProject))

        for pTodo in self.plist["To Dos"] :
            self.todos.append(ToDo(pTodo))

    def addToThings(self):
        for project in self.projects:
            applescript = "tell application \"Things\"\n"
            applescript += project.makeAppleScript()
            applescript += "\nend tell \n"
            self.doAppleScript(applescript)

        for todo in self.todos:
            applescript = "tell application \"Things\"\n"
            applescript += todo.makeAppleScript()
            applescript += "\nend tell \n"
            self.doAppleScript(applescript)

    def doAppleScript(self, applescript):
        cmd = []
        cmd.append("osascript")
        cmd.append("-e")
        cmd.append(applescript)

        process = Popen(cmd, stdout=PIPE)
        out, err = process.communicate()
        print("out:" + str(out))
        print("err:" + str(err))


if __name__ == "__main__":
    obj = thingspy();
    obj.main(sys.argv[1:])