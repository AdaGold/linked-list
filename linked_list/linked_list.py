
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

# Defines the singly linked list


class LinkedList:
    def __init__(self):
        self.head = None  # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: (O)1?
    # Space Complexity: O(1)?

    def get_first(self):
        if self.head == None:
            return None

        return self.head.value

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: (O)1?
    # Space Complexity: O(1)?

    def add_first(self, value):
        # This method adds a new node with the given value to the head of the list
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)?
    # Space Complexity: O(1)?

    def search(self, value):
        # This method returns True or False if the list contains the given value.
        if self.head == None:
            return False

        current = self.head

        while current != None:
            if current.value == value:
                return True
            current = current.next

        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)?
    # Space Complexity: O(1)?

    def length(self):
        # This method returns the size of the list.
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next

        return count

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)?
    # Space Complexity: O(1)?

    def get_at_index(self, index):
        # This method returns the value of the node at the given index. It returns None if the list does not have that many elements.
        if index < 0:
            return None

        current_index = 0
        current = self.head

        while current is not None and current_index < index:
            current = current.next
            current_index += 1

        if current is None:
            return None

        return current.value

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n) ?
    # Space Complexity: O(1)?

    def get_last(self):
        # This method returns the value of the last node in the list.
        if self.head == None:
            return None

        current = self.head

        while current.next != None:
            current = current.next

        return current.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)?
    # Space Complexity: O(n)?

    def add_last(self, value):
        # This method adds a new node to the rear of the list.
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
            return

        current = self.head

        while current.next != None:
            current = current.next

        # new_node = Node(value)
        # current.next = new_node
        current.next = Node(value)

    # method to return the max value in the linked list
    # returns the data value and not the node

    def find_max(self):
        # This method finds the largest value in the list, assuming you can use >, or < to compare each element in the list.
        if self.head == None:
            return None

        current = self.head
        max_value = -100

        while current != None:
            if current.value > max_value:
                max_value = current.value

            current = current.next

        return max_value

    # method to delete the first node found with specified value
    # Time Complexity: O(n)?
    # Space Complexity: O(1)?
    def delete(self, value):

        # If the first node is the one we want to delete, that's a
        # special case.
        if self.head and self.head.value == value:
            self.head = self.head.next
            return

        # Now iterate through the rest of the list and check
        # for the target value at the node _after_ the current one.
        current = self.head
        while current:
            if current.next and current.next.value == value:
                current.next = current.next.next
                return

            current = current.next

    # method to print all the values in the linked list
    # Time Complexity: O(n)?
    # Space Complexity: O(n)?

    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next

        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n) ?
    # Space Complexity: O(1)?

    def reverse(self):
        # If the list is empty or has only one element, then there is nothing to do
        if not self.head or not self.head.next:
            return

        # The list is of length AT LEAST 2. Time to reverse
        # the pointers
        p1 = self.head
        p2 = self.head.next
        p1.next = None  # this is now the end of the new list
        while p2:
            temp = p2.next
            p2.next = p1  # p2 now points at the previous node
            p1 = p2  # advance p1 to the next node (in the old ordering)
            if not temp:  # if we're about to walk off the list, this is the new head
                self.head = p2
            p2 = temp

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

        current.next = self.head  # make the last node link to first node
