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

def find_lowest(start):
    min_value = start.data
    current = start.next
    while current:
        if current.data < min_value:
            min_value = current.data
        current = current.next
    return min_value

def delete_node(head, target):
    current = head

    if head == target:
        return head.next 

    while current.next and current.next != target:
        current = current.next 

    if current.next is None:
        print('target not found')

    current.next = current.next.next 
    return head


#insert new noe
def insert_at_position(head,newnode,position ):
    if position == 1:
        newnode.next = head
        return newnode

    current = head
    for _ in range(position - 2):
        if current is None:
            break
        current = current.next 

    newnode.next = current.next 
    current.next = newnode
    return head



node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(find_lowest(node2))

traversal(node1)

node1 = delete_node(node1,node4)

traversal(node1)
newN = Node(23)
node1 = insert_at_position(node1,newN,4)
traversal(node1)