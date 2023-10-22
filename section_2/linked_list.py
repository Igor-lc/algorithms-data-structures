'''SECTION 2. СТРУКТУРЫ ДАННЫХ. DATA STRUCTURES.
СВЯЗНЫЕ СПИСКИ, LINKED LISTS
Структура данных — это контейнер для организации, хранения и обработки информации. A data structure is a container for organizing, storing, and processing information. И часто качество программного обеспечения и эффективность алгоритмов зависит именно от выбора оптимальной структуры данных. Often, the quality of software and the efficiency of algorithms depend on the choice of an optimal data structure. Поэтому я уделяю им особое внимание. That's why I pay special attention to them. И начнем со связных списков. Одной из самых простых структур. And we'll start with linked lists, one of the simplest data structures. И хотя структура простая, на ее базе можно построить и более сложные представления, вроде графов и деревьев. And even though the structure is simple, you can build more complex representations based on it, such as graphs and trees. Итак, связный список — это последовательность связанных друг с другом объектов в оперативной памяти. So, a linked list is a sequence of interconnected objects in memory. Каждый такой объект называется ячейкой, элементом или узлом и состоит из 2 частей: данных и ссылки на другую ячейку, обычно на следующую. Each of these objects is called a cell, element, or node and consists of two parts: data and a reference to another cell, typically the next one:
75 → 12 → 28 → 6
Такой связный список называется однонаправленным, так как связи работают в одну сторону. Давайте посмотрим на его реализацию на языке Python. This type of linked list is called a singly linked list because the links work in one direction. Let's take a look at its implementation in Python, as shown in the attached photo.
Сперва взглянем на простейший код ячейки связного списка. First, let's examine the simplest code for a linked list node.'''

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)

'''Это обычный пайтон клас, конструктор которого принимает 2 аргумента: value — значение создаваемого узла и next_node – ссылка на следующую ячейку связного списка. По умолчанию оба атрибута принимают None. This is a regular Python class, and its constructor takes two arguments: value, which is the value of the node being created, and next_node, which is a reference to the next cell in the linked list. By default, both attributes are set to None.
Так же клас содержит метод __str__ для вывода значения, которое сохранено в ячейке. The class also contains a __str__ method for displaying the value stored in the cell. Ниже небольшой код, который создаёт связный список. Below is a small code snippet that creates a linked list.'''

node1 = Node(75)
node2 = Node(12)
node1.next_node = node2
node3 = Node(28)
node2.next_node = node3
node4 = Node(6)
node3.next_node = node4

'''Сперва мы создаём узел и он никуда не ссылается, потому что он единственный. First, we create a node, and it doesn't reference anything because it's the only one. Далее мы добавляем еще одну ячейку и после устанавливаем связь. При этом ссылку мы задаём в атрибуте next_node первого узла. Next, we add another cell and establish a connection. We set the reference in the next_node attribute of the first node. То есть при создании каждого узла мы помещаем ссылку на него в значение next_node предыдущего. So, when we create each node, we place a reference to it in the next_node of the previous node. Именно благодаря этим действиям ячейки линкуются и получается связанный список, а не набор отдельных объектов. Попробуем получить значения первого и второго элемента: It's these actions that link the cells and create a linked list, rather than a collection of separate objects. Let's try to retrieve the values of the first and second elements:'''

print(node3.value)
print(node3.next_node.value)

'''Однако, для удобства работы нужен интерфейс для гибкого управления узлами. Обычно для этого используют вспомогательные функции или классы. Мы будем использовать специальный клас List. However, for ease of use, you need an interface for flexible node management. Typically, auxiliary functions or classes are used for this purpose. We will use a special class List:'''

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

'''В нём определено 3 метода: конструктор __init__, append, __str__. Конструктор класса содержит 1 атрибут — ссылку на 1 элемент списка. Который обычно называют top или head. У нас это head. По умолчанию список пустой, поэтому атрибут принимает None. In this class, there are three methods: the constructor __init__, append, and __str__. The class constructor contains one attribute, which is a reference to the first element of the list, usually called top or head. In our case, it's head. By default, the list is empty, so the attribute is set to None`.
Далее следует метод append для добавления нового узла в конец связного списка. Сам узел мы передаем через аргумент метода. Разберем что делает метод. Сперва он устанавливает 1 элемент, если его ещё нет и сразу завершает работу. Если 1 элемент есть, то мы начинаем перебирать все элементы списка до тех пор, пока не дойдём до последнего. Последним будет тот элемент, у которого нет next_node. Соответственно, мы просто устанавливаем для его  next_node ссылку на наш новый элемент, расширяя связнный список справа. Этот алгоритм будет всегда перебирать все элементы списка, а значит его сложность равна О(n). Next is the append method for adding a new node to the end of the linked list. We pass the node itself as an argument to the method. Let's break down what the method does. First, it sets the first element if it doesn't exist and immediately finishes. If there's already a first element, we start iterating through all the elements of the list until we reach the last one. The last element is the one with no next_node. So, we simply set the next_node of the last element to reference our new element, extending the linked list to the right. This algorithm will always iterate through all the elements of the list, making its complexity O(n).
Далее мы реализуем метод __str__ для печати всех элементов связного списка. Он создан просто для вывода информации и не относится напрямую к связным спискам. После применяем класс List() для создания уже знакомого нам списка. Next, we implement the __str__ method for printing all the elements of the linked list. It is created solely for information output and is not directly related to linked lists. After that, we use the List() class to create the familiar list.
Как видите, теперь нам не надо беспокоится об организации связей, класс List() сам обо всём позаботится. Нам лишь надо создать узлы и передать их в метод  append. As you can see, now we don't need to worry about organizing the connections. The List() class takes care of everything for us. All we need to do is create nodes and pass them to the append method.
Как не трудно догадаться, связные списки отлично подходят для хранения данных любых типов и сколь угодно сложных составных структур. При этом сама концепция ссылок на другие элементы позволяет создавать списки любой длины. Встроенные списки в пайтон также позволяют создавать последовательности любой длины, но они не являются связными списками, это скорее динамические массивы. Linked lists are excellent for storing data of any type and as complex composite structures as you like. The concept of references to other elements allows you to create lists of any length. Built-in lists in Python also allow you to create sequences of any length, but they are not linked lists; they are more like dynamic arrays.'''