
from ToDo import ToDo

class Project(ToDo):

    def __init__(self,dict):
        ToDo.__init__(self,dict)
        return