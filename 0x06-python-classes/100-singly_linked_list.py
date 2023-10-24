#!/usr/bin/python3
"""Class Node that defines a node of a singly linked list"""


class Node:
    """
    Represents a node in a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new node.

        Args:
            data (int): The data of the new node.
            next_node: The next node of the new node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the node and ensure it's an integer.

        Args:
            value: The new data for the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node in the list."""
        return self.__next

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node and ensure it's a Node object.

        Args:
            value: The new next node for the current node.

        Raises:
            TypeError: If next_node is not a Node object and is not None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initialize a new singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node with the given value in sorted order."""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while (node.next_node is not None and node.next_node.data < value):
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node

    def __str__(self):
        """Define the string representation of a Singly linked list."""
        result = []
        node = self.__head
        while node is not None:
            result.append(str(node.data))
            node = node.next_node
        return '\n'.join(result)
