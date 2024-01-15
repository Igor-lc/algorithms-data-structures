class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)

class SortedList:
    """
    Sorted linked list
    """

    def __init__(self, value=None, next_node=None):
        self.next_node = next_node
        self.value = value

        # limiters
        self.top = Node()
        self.bottom = Node(1000)
        self.top.next_node = self.bottom

    def append(self, value):
        """
        Adding a new element to a sorted singly linked list.
        Time complexity is O(N).
        """
        # Finding the cell before the cell in which we will insert a new element.
        current = self.top
        while current.next_node.value < value:
            current = current.next_node

        # Inserting a new cell after the current one
        new_node = Node(value)
        new_node.next_node = current.next_node
        current.next_node = new_node


    def sort(self):
        """
         Sorting linked list using the selection sort method.
        """
        # A new limiter is created for the new linked list.
        new_top = Node()

        current = self.top

        # Repeating the while loop as long as the original list is not empty.
        while current.next_node is not None:

            # The "after_me" cell precedes the cell with the maximum value.
            max_after_me = current
            max_value = max_after_me.next_node.value

            # Locating the next element.
            after_me = current.next_node
            while after_me.next_node is not None:
                if after_me.next_node.value > max_value:
                    max_after_me = after_me
                    max_value = after_me.next_node.value
                after_me = after_me.next_node

            # Removing the maximum cell from the original list.
            max_node = max_after_me.next_node
            max_after_me.next_node = max_node.next_node

            

        self.top = new_top

    def __str__(self):
        '''
        Returns all elements of the linked list as a string
        '''
        current = self.top.next_node
        values = "["

        while current is not None and current.value < 1000:
            end = ", " if current.next_node and current.next_node.value < 1000 else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"

sorted_list = SortedList()
sorted_list.append(75)
sorted_list.append(12)
sorted_list.append(28)
sorted_list.append(6)
print(sorted_list)