#!/usr/bin/python3
"""This is the Node class"""


class Node:
    """
    Represents a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
            data (int): The data value to be stored in the node.
            next_node (Node, optional): The next node in the linked list.
            Defaults to None.
        """
        self._data = None
        self._next_node = None
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data value stored in the node.

        Returns:
            int: The data value.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the data value stored in the node.

        Args:
            value (int): The data value to be set.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.

        Returns:
            Node: The next node.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value (Node): The next node to be set.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self._next_node = value


"""
This is the SinglyLinkedList class
"""


class SinglyLinkedList:
    """
    Represents a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position
        in the list (increasing order).

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node is not None and
                   current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        if self.head is None:
            return ""
        current = self.head
        result = ""
        while current is not None:
            if result != "":
                result += "\n"
            result += str(current.data)
            current = current.next_node
        return result
