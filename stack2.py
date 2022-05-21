from collections import deque
stack=deque([1,2,3,4,5])
stack.append("yash")
##STACK FOLLOWS LAST IN FIRST OUT
print(stack)
stack.append(6)
stack.pop()
stack.pop()
stack.pop()

stack.pop()
print(stack)