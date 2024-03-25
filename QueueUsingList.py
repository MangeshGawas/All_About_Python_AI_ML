class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue)==0
    
    def enqueue(self,item):
        self.queue.append(item)
        
        
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
        
    def display(self):
        print(self.queue)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None
        

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)

my_queue.display()
print(my_queue.dequeue())
print(my_queue.dequeue())
my_queue.display()


        


        
