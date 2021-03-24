
# Defines a node in the singly linked list
class Node
  attr_reader :data # allow external entities to read value but not write
  attr_accessor :next # allow external entities to read or write next node

  def initialize(value, next_node = nil)
    @data = value
    @next = next_node
  end
end

# Defines the singly linked list
class LinkedList
    attr_reader :length
    def initialize(node = nil)
      @head = nil # keep the head private. Not accessible outside this class
      @last = nil
      @length = 0
    end

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(value)
      @head = Node.new(value, @head)
      @last = @head if @last.nil?
      @length += 1
    end


    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(value)
      
      node = @head
      while node do 
        return true if node.data == value
        node = node.next
      end
      
      return false
    end

    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_max
      
      return nil if @head.nil? 

      node = @head 
      max = @head.data 

      while node do 
        max = [max, node.data].max
        node = node.next 
      end

      return max 
    end

    # method to return the min value in the linked list
    # returns the data value and not the node
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_min
      return nil if @head.nil? 

      node = @head 
      min = @head.data 

      while node do 
        min = [min, node.data].min
        node = node.next 
      end

      return min
    end


    # Additional Exercises 
    # returns the value in the first node
    # returns nil if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first
      return @head if @head.nil?
      return @head.data
    end

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_last(value)
      if @last.nil?
        add_first(value)
      else
        @last.next = Node.new(value, nil)
        @last = @last.next
        @length += 1
      end
    end

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns nil if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(index, node = @head)
      return nil if index >= self.length
      return node.data if index == 0 || node.next.nil?
      return get_at_index(index - 1, node.next)
    end

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def visit
      node = @head 
      while node do 
        puts node.data
      end
    end

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(value) 
      return nil if @head.nil? 

      if @head.data == value 
        @head = @head.next
        @length -= 1
        return
      end

      current, prev = @head, nil

      while current do 
        if current.data == value 
          prev.next = current.next
          @last = prev if current.next.nil?
          @length -= 1
          return
        end

        prev = current
        current = current.next 
      end
    end

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse
      prev, current, following = nil, @head, @head.next
      @last = @head  
      while current do
        current.next = prev
        prev = current
        @head = current if following.nil? 
        current = following
        if following 
          following = following.next 
        end
      end

    end

    # method that returns the value of the last node in the linked list
    # returns nil if the linked list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_last
      return @last.data
    end
  
    ## Advanced Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def find_middle_value
      raise NotImplementedError
    end

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(n)
      raise NotImplementedError
    end

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle
      raise NotImplementedError
    end

    # method to insert a new node with specific data value, assuming the linked
    # list is sorted in ascending order
    # Time Complexity: ?
    # Space Complexity: ?
    def insert_ascending(value)
      raise NotImplementedError
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
