#this is insertion at the beginning in which we just shift pointers like here we firstly pointed new node as first node then head as this node
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

    def atBeginning(self,data):
        newNode=Node(data)
        newNode.nextval=self.headval
        self.headval=newNode

list=Linked()
list.headval=Node(2)
l0=Node(3)
list.headval.nextval=l0
l1=Node(4)
l2=Node(5)
l3=Node(6)
l0.nextval=l1
l1.nextval=l2
l2.nextval=l3
list.listprint()
list.atBeginning(1)
list.listprint()