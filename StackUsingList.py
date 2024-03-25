class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack)==0
    
    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None
        
    def display(self):
        return self.stack
        

#create my_stack using above class
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(my_stack.display())

print(my_stack.pop())

print(my_stack.peek())

print(my_stack.is_empty())
        
        
    
