
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)
        return
    
    def append_node(self, Node):

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node
        return
    
    def prepend(self, data):

        if self.head is None:
            self.head = Node(data)
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return
    
    def delete(self, data):

        if self.head is None:
            print("Empty List!")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print("Not in List!")
        return
        
    def print_ll(self):

        if self.head is not None:
            current = self.head
        while current is not None:
            print(current.data, end= ' -> ')
            current = current.next
        print('None')

    def reverse(self):

        prev = None
        current = self.head

        while current is not None:

            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(3)
linked_list.append(3)
linked_list.append(3)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.delete(4)
linked_list.delete(2)
linked_list.prepend(0)
linked_list.prepend(0)
linked_list.append(5)


print("Before")
linked_list.print_ll()

# 0, 1, 3, 5, 0 -> 0
#linked_list.append_node(linked_list.head)


def is_cycle(list: LinkedList):

    if not list.head or not list.head.next:
        return False

    slow_pointer = list.head
    fast_pointer = list.head.next
    sp_counter = 0

    while fast_pointer and slow_pointer.next:
    
        if slow_pointer == fast_pointer:
            print("Cycle!")
            return True
        
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        sp_counter += 1

    return False

#is_cycle(linked_list)

def remove_duplicates(linked_list: LinkedList):
    if not linked_list.head:
        return linked_list
        
    seen = set()
    current = linked_list.head
    seen.add(current.data)
    
    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next
            
    return linked_list


removed = remove_duplicates(linked_list)
print("After")
removed.print_ll()



