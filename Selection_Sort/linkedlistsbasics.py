class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(7)
node4 = Node(9)
current_node = node1
node1.next = node2
node2.next = node3
node3.next = node4

print(current_node.data)

while current_node:
    print(current_node.data)
    current_node = current_node.next

