class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


class List:
    def __init__(self):
        # Reference to the first element
        self.head = None

    def append(self, value):
        '''
        Adding a new element to the end of a linked list.
        Operating time O(n).
        '''

        # If there is no first element, create and terminate
        if self.head is None:
            self.head = Node(value)
            return

        # Iterating through all elements sequentially to find the last one
        current = self.head
        while current.next_node is not None:
            current = current.next_node

        # Creating a reference for the last element to the new one
        current.next_node = Node(value)

    def __str__(self):
        '''
        Returns all elements of the linked list as a string
        '''
        current = self.head
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

'''node1 = Node(75)

node2 = Node(12)
node1.next_node = node2

node3 = Node(28)
node2.next_node = node3

node4 = Node(6)
node3.next_node = node4

print(node4.value)
print(node4.next_node.value)'''
