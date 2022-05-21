class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class LinkList:
    def __init__(self):
        self.headval=None

    def printL(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

head=LinkList()
head.headval=Node(5)
L1=Node(6)
L2=Node(7)
L3=Node(8)
head.headval.nextval=L1
L1.nextval=L2
L2.nextval=L3
head.printL()
