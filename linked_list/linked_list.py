
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
      self.head = None # keep the head private. Not accessible outside this class
      self.size = 0
      self.tail = None

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(n)
    def get_first(self):
        if self.head == None:
            return None
        return self.head.value    


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        current = self.head
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
        else:
            new_node = Node(value)
            new_node.next = current
            current.previous = new_node
            self.head = new_node
            self.size += 1

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current = self.head 
        while current != None:
            if current.value == value:
                return True 
            current = current.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def length(self):
        return self.size
        

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: ?
    # Space Complexity: ?
    def get_at_index(self, index):
        length = self.length()
        current = self.head
        counter = 0
        if self.head == None and length < index:
            return None

        while current:
            if index == counter:
                return current.value
            counter += 1
            current = current.next

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(n)
    def get_last(self):
        #if self.head == None:
        #    return None
        #current = self.head 
        #while current.next != None:
        #    current = current.next
        #return current.value 
        if self.head == None:
            return None

        return self.tail.value
        
    # this may be improved using a tail node 

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        #new_node = Node(value)
        #curr = self.head

        #if curr is None:
        #    self.head = new_node
        #else:
        #    while curr.next is not None:
        #        curr = curr.next
        #    curr.next = new_node

        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.size += 1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            # current.previous = current.next
            current.next = new_node
            self.tail = new_node
            self.size += 1
# testing? 
    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        current = self.head 
        max = 0
        if self.head == None:
            return None
        while current != None:
            if max < current.value:
                max = current.value
            current = current.next
        return max        



    # method to delete the first node found with specified value
    # Time Complexity: O(n) 
    # Space Complexity: O(1)
    def delete(self, value):
        current = self.head
        if current == None:
            return
        if current.value == value:
            self.head = self.head.next
            self.size -= 1
            self.head.previous = None
            return

        while current:
            if current.next == None:
                if current.value == value:
                    previous = current.previous
                    self.tail = previous
                    previous.next = None
                    current.previous = None
                    current = None
                    self.size -= 1
                    return
            if current.value == value:
                next = current.next
                previous = current.previous
                next.previous = previous
                current.previous = None
                current.next = None
                self.size -= 1
                return

            current = current.next


    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        current = self.head 
        previous = None 
        while current != None:
            next = current.next 
            current.next = previous
            previous = current
            current = next 
        self.head = previous     
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def find_middle_value(self):
        pass

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        pass

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
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
