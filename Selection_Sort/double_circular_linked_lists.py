class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)
node5 = Node(9)

current = node1
node1.next =  node2
node1.prev = node5

node2.next = node3
node2.prev = node1

node3.next = node4
node3.prev = node2

node4.next = node5
node4.prev = node3 

node5.next = node1
node5.prev = node4

startnode= node1

print(current.data)
current = current.next 

while current != startnode:
    print(current.data)
    current = current.next 
print('List done in forward.')

current = node5
startnode = node5

print(current.data)
current = current.prev

while current != startnode :
    print(current.data)
    current = current.prev
print('list done in backwards.')




