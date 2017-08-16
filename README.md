# Linked-List
Using object oriented design constructs, define a Node class and LinkedList class for a singly linked list. Each node has integer data value and a link to the next node. The linked list class has a head node and the following methods defined.

## Exercise
Design and implement the classes and the methods.
Methods to implement in the singly linked list:
  - *insert*: method to add a new node with the specific input data value in the linked list. 
              Insert the new node at the beginning of the linked list
  - *search*: method to find if the linked list contains a node with specified input value. Returns true if found, false otherwise.
  - *find_max*: method to return the max value in the linked list. Returns the data value and not the node.
  - *find_min*: method to return the min value in the linked list. Returns the data value and not the node.
  - *length*: method that returns the length of the singly linked list
  - *find_nth_from_beginning*: method to return the value of the nth element from the beginning. n is the input to the method.
                             Assume indexing starts at 0 while counting to n.
  - *insert_ascending*: method to insert a new node with specific input data value, assuming the linked list is sorted in ascending order.
  - *visit*: method to print all the values in the linked list
  - *delete*: method to delete the first node found with the specified value taken as input.
  - *reverse*: method to reverse the singly linked list. The nodes should be moved and not just the values in the nodes.

  ## Advanced Exercises
  - *find_middle_value*: Returns the value at the middle element in the singly linked list.
                       If the node count is even, return the average of the two middle values.
  - *find_nth_from_end*: find the nth node from the end and return its value. Assume indexing starts at 0 while counting to n.
  - *has_cycle*: Checks if the linked list has a cycle. A cycle exists if any node in the linked list links to a node already visited.  
               Returns true if a cycle is found, false otherwise.
  
