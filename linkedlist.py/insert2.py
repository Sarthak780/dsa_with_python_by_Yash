
#this code is for insertion at the end of a singlyt linked list
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class Linked:
    def __init__(self):
        self.headval=None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval 

    def atEnd(self,newdata):
        if self.headval==None:
            self.headval=Node(newdata)
            return
        endval=self.headval
        while(endval.nextval):
            endval=endval.nextval
        endval=Node(newdata)

list =Linked()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.AtEnd("Thu")

list.listprint()

