from collections import deque
 
myStack.append("a")
myStack.append("b")
myStack.append("c")
myStack.append("d")
print(myStack)
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
##
##deque implementation is mush better for append and pop function as deque is implemented over linked list so it takes constant time for append and pop due to nodes pointing towards both direction

