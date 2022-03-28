
# Defines a node in the singly linked list
from hashlib import new


class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    def get_first(self):
        if not self.head:
            return

        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    def add_first(self, value):
        self.head = Node(value, self.head)


    # method to find if the linked list contains a node with specified value
    def search(self, value):
        current = self.head
        
        while current != None:
            if current.value == value:
                return True
            current = current.next

        return False


    # method that returns the length of the singly linked list
    def length(self):
        count = 0
        current = self.head

        while current != None:
            count +=1
            current = current.next
        return count


    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    def get_at_index(self, index):
        count = 0
        current = self.head

        while current != None:
            if count == index:
                return current.value
            count +=1
            current = current.next
        return None


    # method that returns the value of the last node in the linked list
    def get_last(self):
        if not self.head:
            return
        
        current = self.head
        while current.next != None:
            current = current.next
        return current.value
        

    # method that inserts a given value as a new last node in the linked list
    def add_last(self, value):
        if not self.head:
            self.add_first(value)
        else:
            new_node = Node(value)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        max_value = 0
        current = self.head

        if not self.head:
            return

        while current != None:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value


    # method to delete the first node found with specified value
    def delete(self, value):
        if not self.head:
            return
        # removing first node
        elif self.head.value == value:
            self.head = self.head.next
            return
        else:
            current = self.head
            # while next node != null and next value != value reassign current value until found
            while current.next and current.next.value != value: 
                current = current.next 
            current.next = current.next.next



    # method to print all the values in the linked list
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))


    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next = current.next
            current.next = previous # reverses direction of pointer
            previous = current # previous value continues to stack before current
            current = next # iterates until end of list

        self.head = previous # last previous value is the head of the list now
    

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    def find_middle_value(self):
        if not self.head:
            return
        return self.get_at_index(int(self.length() // 2))


    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    def find_nth_from_end(self, n):
        count = 0
        current = self.head

        if self.length() < n:
            return

        while current and count < n:
            current = current.next
            count += 1

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    def has_cycle(self):
        pass


    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
