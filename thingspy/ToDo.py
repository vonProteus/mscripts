import hashlib

class ToDo:
    def __init__(self, dict):
        self.plist = dict
        self.md5 = "md5"
        self.md5 += str(hashlib.md5(str(self.plist)).hexdigest())
        return

    def getName(self):
        return self.plist["name"]

    def getNotes(self):
        if "notes" not in self.plist:
            return ""
        return self.plist["notes"]

    def getTags(self):
        if "tags" not in self.plist:
            return []
        return self.plist["tags"]

    def getDueDate(self):
        if "due date " not in self.plist:
            return 0
        return self.plist["due date "]

    def getMD5(self):
        return self.md5

    def getMD5Mark(self, mark):
        return self.md5 + str(hashlib.md5(str(mark)).hexdigest())

    def makeAppleScript(self):
        ans = "\n"

        ans += "set " + self.getMD5() +" to make new to do \n"

        ans += "set name of " + self.getMD5() + " to \""+ self.getName() +"\"\n"

        ans += "set notes of " + self.getMD5() + " to \""+ self.getNotes() +"\"\n"

        if self.getDueDate() > 0 :
            ans += "set due date of " + self.getMD5() + " to (current date) + "+ str(self.getDueDate()) +" * days\n"

        tags = ""
        for tag in self.getTags():
            ans += "set "+self.getMD5Mark(tag)+" to make new tag with properties {name:\""+tag+"\"} \n"
            tags+= tag + ", "

        if tags != "" :
            tags = tags[:-2]
            ans += "set tag names of " + self.getMD5() + " to \""+ tags +"\"\n"

        return ans

