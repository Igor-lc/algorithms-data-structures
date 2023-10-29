class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)

class List:
    def __init__(self):
        # limiter
        self.top = Node()
        self.tail = None

    def append(self, value):
        '''
        Adding a new element to the end of a linked list.
        Operating time O(n).
        '''

        # Iterating through all elements sequentially to find the last one
        current = self.top
        while current.next_node is not None:
            current = current.next_node

        # Creating a reference for the last element to the new one
        current.next_node = Node(value)

    def __str__(self):
        '''
        Returns all elements of the linked list as a string
        '''
        current = self.top.next_node
        values = "["
        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"

lst = List()
lst.append(75)
lst.append(12)
lst.append(28)
lst.append(6)
print(lst)