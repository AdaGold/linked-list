# Linked-List

Using object oriented design constructs, define a Node class and LinkedList class for a singly linked list. Each node has integer data value and a link to the next node. The linked list class has a head node and the following methods defined.

## Getting Started

As usual with a python project, create a virtual environment:

```
python3 -m venv venv
```

Then activate the virtual environment

```
source venv/bin/activate
```

Then install the required packages.

```
pip install -r requirements.txt
```

## Exercise

Design and implement the classes and the methods. Implement the methods within the Linked List class that are currently only contain `pass`.

Complete the following methods:

* `get_first` - This method returns the value of the 1st node in the list (head).  It returns `None` if the list is empty.
* `add_first` - This method adds a new node with the given value to the head of the list.
* `search` - This method returns `True` or `False` if the list contains the given value.
* `length` - This method returns the size of the list.
* `get_at_index` - This method returns the value of the node at the given index.  It returns `None` if the list does not have that many elements.
* `get_last` - This method returns the value of the last node in the list.
* `add_last` - This method adds a new node to the rear of the list.
* `find_max` - This method finds the largest value in the list, assuming you can use `>`, or `<` to compare each element in the list.
* `delete` - This method deletes the node at the given index maintaining all the remaining elements in the same order.
* `reverse` - This method reverses the list.

### Going Further

There are a set of advanced methods you can choose to implement for additional practice.  Tests are provided, but you will need to unskip them by removing the `@pytest.mark.skip` decorator.

For more practice complete the following methods:

* `find_middle_value` - This method returns the value in the middle of the list (rounded down for even length lists).
* `find_nth_from_n` - This method returns the value of the node which is nth from last in the list.
* `has_cycle`- This method returns true if there is a loop in the list.  I.e. somehow a node's next value is pointing to a prior node.
