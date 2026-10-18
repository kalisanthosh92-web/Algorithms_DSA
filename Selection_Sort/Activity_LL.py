#singly linked lists
class SNode:
    def __init__(self,data):
        self.data = data
        self.next = None

def display():
    current = node1
    while current:
        print(current.data, end = ' -> ')
        current = current.next
    print('None')


def search(target):
    current = node1
    print(f'Searching for {target}:')
    while current:
        if current.data == target:
            return f'{target} Found!'
        current = current.next
    return 'notfound!'


def delete_node(head, target):
    head = node1
    current = head

    if head == target:
        return head.next 

    while current.next and current.next != target:
        current = current.next 

    if current.next is None:
        print('target not found')

    current.next = current.next.next 
    return head



node1 = SNode('Quiz')
node2 = SNode('Laboratory Exercise')
node3 = SNode('Midterm Examination')
node4 = SNode('Project')
node5 = SNode('Presentation')


current = node1
node1.next =  node2
node2.next = node3
node3.next = node4
node4.next = node5


