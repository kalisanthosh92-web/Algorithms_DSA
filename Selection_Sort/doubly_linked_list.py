class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)

current_node = node1
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3

#Traversing Forward
while current_node:
    print(current_node.data)
    current_node = current_node.next
print('Done!')

#Traversing Backward
current_node = node4
while current_node:
    print(current_node.data)
    current_node = current_node.prev
print('Done in backwards!')


