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
        if self.head is None:
            return None
        else: 
            return self.head.value

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
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False
            

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        node_count = 0
        current_node = self.head
        while current_node is not None:
            node_count += 1
            current_node = current_node.next
        return node_count

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        current_node = self.head
        current_index = 0

        if current_node is None:
            return None
        
        while current_node is not None:
            if current_index == index:
                return current_node.value
            else:
                current_node = current_node.next
                current_index+=1
        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        current_node = self.head

        if current_node is None:
            return None
        
        while True:
            if current_node.next is None:
                return current_node.value
            else:
                current_node = current_node.next

        

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        new_node = Node(value)
        current_node = self.head

        if current_node is None:
            self.head = new_node
            return

        # What do I want while loop to do? I want while loop to find the last node 

        while current_node is not None:
            if current_node.next is None:
                break
            current_node = current_node.next 

        # When last node is found, I want to append new_node to it.
        current_node.next = new_node

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        current_node = self.head
        if current_node is None:
            return None

        max_value = current_node.value

        while current_node.next:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next

        if current_node.value > max_value:
            max_value = current_node.value
              
        return max_value

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        current_node = self.head
        previous_node = None

        if current_node is None:
            return None

        # Case: value to be deleted is the first value in the linked list
        if current_node.value == value:
            self.head = current_node.next
            current_node = None
            return
        
        # Case: value to be deleted is the last value in the linked list
            # traverse linked list to find the last node
            # compare speficied value to last node's value
            # if the values match, re-assign the penultimate node reference to None
        while current_node is not None and current_node.value != value:
            previous_node = current_node
            current_node = current_node.next
        
        previous_node.next = current_node.next
        current_node = None
            
            

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
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
    # Space Complexity: O(n)
    def reverse(self):

        # Put nodes in a list
        # Reverse the list
        # Create a new linked list from the reversed list
        
        current_node = self.head
        nodes_list = []
        nodes_list_reverse = []

        while current_node is not None:
            nodes_list.append(current_node)
            current_node = current_node.next

        i = len(nodes_list)-1

        while i > 0:
            nodes_list_reverse.append(nodes_list[i])
            i -= 1
        nodes_list_reverse.append(nodes_list[0])

        for i in range(0, len(nodes_list_reverse)):
            if i == 0:
                current_node = nodes_list_reverse[i]
                self.head = current_node
            else:
                current_node = nodes_list_reverse[i]

            if i < len(nodes_list_reverse)-1:
                current_node.next = nodes_list_reverse[i+1]
            
        current_node.next = None

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
