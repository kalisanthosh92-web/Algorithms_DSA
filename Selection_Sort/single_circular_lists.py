class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)
node5 = Node(9)

current = node1
node1.next =  node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node1


startnode = node1
print(current.data)
current = current.next

while current != startnode:
    print(current.data)
    current = current.next

print("Loop done!")
