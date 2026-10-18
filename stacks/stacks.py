class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty."
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty."
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0 

    def size(self):
        return len(self.stack)

#Create a stack.
mystack = Stack()

mystack.push('A')
mystack.push('B')
mystack.push('C')

print('Stack: ', mystack.stack)

print('poped element: ', mystack.pop())

print("peek: ", mystack.peek())

print('size: ', mystack.size())

print('isempty: ', mystack.isEmpty())
