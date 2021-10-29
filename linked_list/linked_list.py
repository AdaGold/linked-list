
# Defines a node in the singly linked list
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
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head:
            return self.head.value
        else: 
            return None

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        if not self.head:
            return False
        else:
            curr_node = self.head
            while curr_node != None:
                if curr_node.value == value:
                    return True
                curr_node = curr_node.next
            return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        curr_node = self.head
        len = 0
        while curr_node != None:
            len += 1
            curr_node = curr_node.next
        return len

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        if index >= self.length():
            print("The index is out of range")
            return None
        curr_index = 0
        curr_node = self.head
        while index > curr_index:
            curr_node = curr_node.next
            curr_index += 1
        if curr_index == index:
            return curr_node.value

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if not self.head:
            return None
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        return curr_node.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = new_node

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if not self.head:
            return None
        curr_node = self.head
        max_value = self.head.value
        while curr_node != None:
            if curr_node.value > max_value:
                max_value = curr_node.value
            curr_node = curr_node.next
        return max_value

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        if not self.head:
            return None
        curr_node = self.head
        if value == curr_node.value:
            self.head = curr_node.next
            return
        while curr_node != None:
            prev_node = curr_node
            curr_node = curr_node.next
            if value == curr_node.value:
                prev_node.next = curr_node.next
                return 

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def visit(self):
        helper_list = []
        curr_node = self.head

        while curr_node:
            helper_list.append(str(curr_node.value))
            curr_node = curr_node.next
        
        print(", ".join(helper_list))
        return helper_list

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        len_list = self.length()
        index = len_list // 2
        return self.get_at_index(index)

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        len_list = self.length()
        index = len_list - 1 - n
        return self.get_at_index(index)

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def has_cycle(self):
        slow_p = self.head
        fast_p = self.head
        while fast_p and fast_p.next != None:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
        return False

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next

        curr_node.next = self.head # make the last node link to first node

