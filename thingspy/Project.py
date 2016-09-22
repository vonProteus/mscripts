
from ToDo import ToDo

class Project(ToDo):

    def __init__(self,dict):
        ToDo.__init__(self,dict)
        self.todos = []

        if "to dos" in self.plist:
            for pToDo in self.plist["to dos"]:
                self.todos.append(ToDo(pToDo))

        return

    def getArea(self):
        if "area" not in self.plist:
            return ""
        return self.plist["area"]

    def getTodos(self):
        return self.todos

    def makeAppleScript(self):
        ans = "\n"

        ans += "set " + self.getMD5() + " to make new project  \n"

        ans += "set name of " + self.getMD5() + " to \"" + self.getName() + "\"\n"

        if self.getArea() != "" :
            # ans += "set " + self.getMD5Mark(self.getArea()) + " to make new area with properties {name:\"" + self.getArea() + "\"} \n"
            ans += "set area of " + self.getMD5() + " to area \"" + self.getArea() + "\"\n"

        ans += "set notes of " + self.getMD5() + " to \"" + self.getNotes() + "\"\n"

        if self.getDueDate() > 0:
            ans += "set due date of " + self.getMD5() + " to (current date) + " + self.getDueDate() + " * days\n"

        tags = ""
        for tag in self.getTags():
            ans += "set "+self.getMD5Mark(tag)+" to make new tag with properties {name:\""+tag+"\"} \n"
            tags += tag + ", "

        if tags != "":
            tags = tags[:-2]
            ans += "set tag names of " + self.getMD5() + " to \"" + tags + "\"\n"

        for todo in self.getTodos():
            ans += todo.makeAppleScript()
            ans += "set project of "+ todo.getMD5() +" to " + self.getMD5()

        return ans