
# Defines a node in the singly linked list
class Node
  attr_reader :data # allow external entities to read value but not write
  attr_accessor :next # allow external entities to read or write next node

  def initialize(value)
    @data = value
    @next = nil
  end
end

# Defines the singly linked list
class LinkedList
    def initialize
      @head = nil # keep the head private. Not accessible outside this class
    end
  
    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    def add_first(value)
        new_node = Node.new(value)
  
        if @head != nil # if linked list is not empty
          new_node.next = @head
        end
  
        @head = new_node
    end
  
    # returns the value in the first node
    # returns nil if the list is empty
    def get_first
      return nil if !@head
      return @head.data
    end
  
    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    def search(value)
        current = @head
        while current != nil
          if current.data == value
            return true
          end
          current = current.next
        end
  
        return false
    end
  
    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max
        if @head == nil # empty list case
          # puts "Error: The linked list is empty. Cannot compute max."
          return nil
        end
  
        current = @head
        max = current.data
        current = current.next
        while current != nil
          if current.data > max
            max = current.data
          end
          current = current.next
        end
        return max
    end
  
    # method to return the min value in the linked list
    # returns the data value and not the node
    def find_min
        if @head == nil # empty list case
          # puts "Error: The linked list is empty. Cannot compute min."
          return nil
        end
  
        current = @head
        min = current.data
        current = current.next
        while current != nil
          if current.data < min
            min = current.data
          end
          current = current.next
        end
        return min
    end
  
    # method that returns the length of the singly linked list
    def length
        count = 0
        current = @head
        while current != nil
          count += 1
          current = current.next
        end
  
        return count
    end
  
    # method that inserts a given value as a new last node in the linked list
    def add_last(value)
      new_node = Node.new(value)
  
      if !@head
          @head = new_node
          return
      end
  
      current = @head
      while current.next
          current = current.next
      end
      current.next = new_node
      return
    end
  
    # method that returns the value of the last node in the linked list
    # returns nil if the linked list is empty
    def get_last
      return nil if !@head
      current = @head
      while current.next
          current = current.next
      end
      return current.data
    end
  
    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns nil if there are fewer nodes in the linked list than the index value
    def get_at_index(index)
        i = 0
        current = @head
        while current != nil
          if i == index
            return current.data
          end
          current = current.next
          i += 1
        end
        # puts "Error: #{index} exceeds the linked list length."
        return nil
    end
  
  
    # method to insert a new node with specific data value, assuming the linked
    # list is sorted in ascending order
    def insert_ascending(value)
        new_node = Node.new(value)
  
        # check for new_node being the new head case
        if @head == nil || value <= @head.data
          new_node.next = @head
          @head = new_node
          return
        end
  
        current = @head
        while current.next != nil && current.next.data < value
          current = current.next
        end
        new_node.next = current.next
        current.next = new_node
    end
  
    # method to print all the values in the linked list
    def visit
        current = @head
        while current != nil
          print "#{current.data} "
          current = current.next
        end
        puts
    end
  
    # method to delete the first node found with specified value
    def delete(value)
        if @head == nil
          return
        end
  
        # account for case: node to delete is current head
        if @head.data == value
          @head = @head.next
          return
        end
  
        current = @head
        while current.next != nil
          if current.next.data == value
            current.next = current.next.next
            return
          end
          current = current.next
        end
        # value to be deleted was not found if the control flow reaches here
    end
  
    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    def reverse
        current = @head
        previous = nil
        while current != nil
          temp = current.next # save state
          current.next = previous # update link
  
          # move to next
          previous = current
          current = temp
        end
        @head = previous
    end
  
    ## Advanced Exercises
    # returns the value at the middle element in the singly linked list
    def find_middle_value
        if @head == nil
          return nil
        end
  
        slow = @head
        fast = @head.next
        while fast != nil
          slow = slow.next
          fast = fast.next
          if fast != nil
            fast = fast.next
          end
        end
        return slow.data
    end
  
    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    def find_nth_from_end(n)
        # approach with going through the linked list just once
        current = @head
        index = 0
        # count to n from the beginning
        while current != nil && index != n
          current = current.next
          index += 1
        end
  
        # check that we didn't reach the end
        if current == nil
          # puts "Error: The linked list has less than #{n} indexable nodes"
          return nil
        end
  
        # the previous while loop exited because of index == n condition
        # start a new traverser at the beginning.
        # when current reaches the end, new_current will be at index n from the end
        new_current = @head
        while current.next != nil
          current = current.next
          new_current = new_current.next
        end
        return new_current.data
    end
  
    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    def has_cycle
        if @head == nil || @head.next == nil
          return false
        end
        slow = @head
        fast = @head
        while fast != nil
          slow = slow.next
          fast = fast.next
          if fast != nil
            fast = fast.next
          end
          if slow == fast
            return true # cycle detected
          end
        end
        return false # reached the end of the linked list - no cycle detected
    end
  
    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle
      return if @head == nil # don't do anything if the linked list is empty
  
      # navigate to last node
      current = @head
      while current.next != nil
        current = current.next
      end
  
      current.next = @head # make the last node link to first node
    end
  end
  
