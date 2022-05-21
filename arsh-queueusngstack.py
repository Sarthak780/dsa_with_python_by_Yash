class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x):
        self.inStack.append(x)

    def pop(self):
        if self.outStack == []:
            for _ in range(len(self.inStack)):
                element = self.inStack.pop()
                self.outStack.append(element)
        return self.outStack.pop()
            
    def peek(self):
        if self.outStack == []:
            for _ in range(len(self.inStack)):
                element = self.inStack.pop()
                self.outStack.append(element)
        return self.outStack.pop()
    def empty(self):
        if self.inStack == [] and self.outStack == []:
            return True
        return False
        



obj = MyQueue()
obj.push(12)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()