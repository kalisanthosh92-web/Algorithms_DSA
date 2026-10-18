#in a singly linked lists 
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


def traversal(head):
    current = head
    while current:
        print(current.data, end = '->')
        current = current.next
    print("Null")


node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traversal(node1)
