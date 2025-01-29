class Node:
    def __init__(self, data):
        self.data = data # the node has some data
        self.next = None # and a pointer to the next node

class LinkedList:

    def __init__(self):
        self.head = None # the LL needs a head, where it starts

    def append(self, value):

        # if the LL has no head yet, we create it
        if self.head is None:
            self.head = Node(value)
            return

        # if it has a head, we set current to the head, traverse it until the end and create a new node which is pointed on by our current (last) node
        current = self.head 
        while current.next is not None:
            current = current.next
        current.next = Node(value)
        return

    def prepend(self, value):

        # if we want to prepend, we effectively create a new head node.
        newhead = Node(value)

        # we then set the new head nodes pointer to the current head
        newhead.next = self.head

        # and finally update the LLs head to the newhead
        self.head = newhead
        return

    def delete(self, value):

        # if there is no head, just return as there is nothing to delete
        if self.head is None:
            return
        
        # if the value I want to delete is actually the heads value, cut it out
        if self.head.data == value: 
            self.head = self.head.next
            return
        
        # we take the current node, which is the head, traverse until the end. 
        # If we see that the next nodes value is the one we want to delete, update the pointers to work around the next node, otherwise move on
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return
            else:
                current = current.next

    def print_list(self):

        if self.head is None:
            print("Linked List is empty")

        else:
            current = self.head
            while current is not None:
                print(current.data, end=' -> ')
                current = current.next
            print("None")


# merge 2 sorted linked lists
def merge(l1: Node, l2: Node) -> Node:
        
    head = Node(0)
    current = head
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
            current = current.next
        else:
            current.next = l2
            l2 = l2.next
            current = current.next
            
    if l1:
        current.next = l1
    elif l2:
        current.next = l2
    
    head = head.next
    
    return head

# Demonstrative usage
def main():
    
    my_ll = LinkedList()
    my_ll.print_list()

    my_ll.append(3)
    my_ll.append(2)
    my_ll.append(1)
    my_ll.prepend(0)
    my_ll.print_list()

if __name__ == "__main__":
    
    main()