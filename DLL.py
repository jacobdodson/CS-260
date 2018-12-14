#Linked list node
class Node:
    def __init__(self, data):
        """Constructor for a new node"""
        self.data = data
        self.next = None
        self.prev = None

#Doubly Linked list class
class DoublyLinkedList:

    def __init__(self):
        """Constructor for empty list"""
        self.head = None
        self.end = None
        self.length = 0

    def prepend(self, new_data):
        """Using the reference to the head of a list and an
        integer, inserts a new node on the front of the list"""
        new_node = Node(new_data)

        if self.head is None:
            new_node.prev = None
            self.head = new_node

        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

        self.length += 1

    def append(self, new_data):
        """Using the reference to the head of a list and an
        integer, inserts a new node on the end of the list"""
        new_node = Node(new_data)

        if self.head is None:
            new_node.prev = None
            self.head = new_node

        else:
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node
            new_node.next = None
            self.end = new_node

        self.length += 1

    def insert(self, new_data, index):
        """Insert a new node with the data (new_data) at that index(index)"""
        new_node = Node(new_data)

        if index > self.length:
            raise IndexError("Index out of range")

        elif index == 0:
            self.prepend(new_data)

        elif index == self.length:
            self.append(new_data)

        else:
            next_node = self.node_at(index)
            new_node.next = next_node
            new_node.prev = next_node.prev
            next_node.prev.next = new_node
            next_node.prev = new_node

        self.length += 1

    def pop(self):
        """Using the reference to the end of the list we
        pop(remove) off the last node"""

        if self.end is None:
            raise IndexError("List is empty")

        else:
            current_node = self.end
            temp_node = current_node.prev

            current_node.prev = None
            temp_node.next = None
            self.end = temp_node

            self.length -= 1

    def remove(self):
        """Remove a node at the front of the list"""
        if self.head is None:
            raise IndexError("List is empty")

        else:
            current_node = self.head
            temp_node = current_node.next

            current_node.next = None
            temp_node.prev = None
            self.head = temp_node


    def node_at(self, index):
        """Returns a reference to the indexed node"""
        if index == -1:
            return None

        if index > self.length or index < -1:
            raise IndexError("Index out of range")

        current_node = self.head
        for j in range(index):
            current_node = current_node.next

        return current_node

    def get_length(self):
        """Returns length of list"""
        return self.length

    def print_list(self):
        """Using the reference to the head of a list, traverses down
        the list and prints each nodes data until the end"""
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.insert(4, 2)
dllist.remove()
dllist.print_list()

