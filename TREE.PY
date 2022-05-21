class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None


node1=BinaryTree(10)
node2=BinaryTree(20)
node3=BinaryTree(30)
node4=BinaryTree(40)
node5=BinaryTree(50)
node6=BinaryTree(60)
node7=BinaryTree(70)
node8=BinaryTree(80)

node1.leftChild=node2
node1.rightChild=node3
node2.leftChild=node4
node2.rightChild=node5
node3.leftChild=node6
node3.rightChild=node7
print("root node is " ,node1.data)
print("leftchild of root node1 is ", node1.leftChild.data)
print("right child of root node1 is ", node1.rightChild.data)
print("leftchild of node2 is ", node2.leftChild.data)
print("right child of node2 is ", node2.rightChild.data)
print("leftchild of node3 is ", node3.leftChild.data)
print("right child of  node3 is ", node3.rightChild.data)








