class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None

    def __str__(self):
        return f'({self.key}, {self.value})'

class List:

    def __init__(self):
        self.head = None

    def append(self, key, value):
        if self.head is None:
            self.head = Node(key, value)
            return

        current = self.head
        while current.next_node is not None:
            current = current.next_node

        current.next_node = Node(key, value)

    def find(self, key, key_end=None):
        if key_end is None:
            key_end = key
        current = self.head

        values, data, i = {}, 1, 0

        while current is not None:
            if isinstance(key, int) and isinstance(current.key, int):
                if key <= current.key <= key_end:
                    values[i] = current.value
                    data = 0
                    i += 1
            elif isinstance(key, str) and isinstance(current.key, str):
                if key <= current.key <= key_end:
                    values[i] = current.value
                    data = 0
                    i += 1

            current = current.next_node
        return None if data else (values.values() if values else '')


lst = List()
lst.append(1, "A")
lst.append(2, "B")
lst.append(3, "C")
lst.append(4, "")
lst.append("ABC", 1)

print(lst.find(1, 3)) 
print(lst.find(4))
print(lst.find(5))
print(lst.find("ABC"))
