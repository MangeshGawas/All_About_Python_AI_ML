#Create a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous Node is not present")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, "->", end=" ")
            current_node = current_node.next
        print("None")
    

linkedList1 = LinkedList()
linkedList1.append(1)
linkedList1.append(2)
linkedList1.prepend(0)
linkedList1.insert_after_node(linkedList1.head.next,1.5)
linkedList1.display()
        