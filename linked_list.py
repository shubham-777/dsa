"""
Author      : Shubham Ahinave
Created at  : 22/07/24
Desc        : A Python implementation of a singly linked list and operations on it.

              This module defines two classes: Node and LinkedList. Node represents a single element
              in the linked list containing data and a reference to the next node. LinkedList manages
              the nodes, allowing operations like appending, deleting, inserting, searching, getting
              size, traversing, and swapping nodes.

              Example usage:
                  ll = LinkedList()
                  [ll.append(data=i) for i in range(11)]
                  print(ll.travers())
                  ll.delete(value=3)
                  print(ll.travers())
                  ll.insert_at(data=55, index=5)
                  print(ll.travers())
                  ll.swap_by_value(value_a=1, value_b=7)
                  print(ll.travers())
                  ll.swap_by_index(idx_a=0, idx_b=ll.size() - 1)
                  print(ll.travers())

              Classes:
                  Node: Represents a node in a singly linked list.
                  LinkedList: Represents a singly linked list and provides operations on it.
"""


class Node:
    """Class representing a node in a linked list."""

    def __init__(self, data):
        """
        Initialize a node with data.

        Args:
            data: Data to be stored in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """Class representing a singly linked list."""

    ll_operator = ' -> '

    def __init__(self, head=None):
        """
        Initialize the linked list with an optional head node.

        Args:
            head: Optional initial node of the linked list.
        """
        self.head = head

    def append(self, data):
        """
        Append a new node with the given data to the end of the linked list.

        Args:
            data: Data to be stored in the new node.
        """
        node = Node(data=data)
        if self.head:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = node
        else:
            self.head = node

    def delete(self, value):
        """
        Delete the first occurrence of a node with the given value.

        Args:
            value: Value to be deleted from the linked list.
        """
        curr_node = self.head
        if curr_node.data == value:
            self.head = curr_node.next
            return
        prev_node = None
        while curr_node.next:
            if curr_node.data == value:
                break
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node.data == value:
            prev_node.next = curr_node.next

    def insert_at(self, data, index):
        """
        Insert a new node with the given data at a specified index.

        Args:
            data: Data to be stored in the new node.
            index: Index at which to insert the new node.
        """
        curr_node = self.head
        new_node = Node(data=data)
        if index == 0:
            new_node.next = curr_node
            self.head = new_node
            return

        iter_idx = 0
        prev_node = None
        while curr_node.next:
            iter_idx += 1
            prev_node = curr_node
            curr_node = curr_node.next
            if iter_idx == index:
                break
        if iter_idx == index:
            prev_node.next = new_node
            new_node.next = curr_node

    def search(self, value):
        """
        Search for the first occurrence of a node with the given value.

        Args:
            value: Value to search for in the linked list.

        Returns:
            Index of the node containing the value.
        """
        linked_lst_as_str = self.travers()
        linked_lst_data = linked_lst_as_str.split(self.ll_operator)
        return linked_lst_data.index(str(value))

    def get_by_index(self, index):
        """
        Retrieve the data of the node at the specified index.

        Args:
            index: Index of the node to retrieve.

        Returns:
            Data stored in the node at the specified index.
        """
        iter_idx = 0
        curr_node = self.head
        while curr_node.next:
            if index == iter_idx:
                break
            curr_node = curr_node.next
            iter_idx += 1
        return curr_node.data

    def size(self):
        """
        Get the size (number of nodes) of the linked list.

        Returns:
            Size of the linked list.
        """
        linked_lst_as_str = self.travers()
        linked_lst_data = linked_lst_as_str.split(self.ll_operator)
        return len(linked_lst_data)

    def travers(self):
        """
        Traverse the linked list and return its representation as a string.

        Returns:
            String representation of the linked list.
        """
        curr_node = self.head
        linked_lst = str(curr_node.data)
        while curr_node.next:
            curr_node = curr_node.next
            linked_lst = linked_lst + self.ll_operator + str(curr_node.data)
        return linked_lst

    def swap_by_index(self, idx_a, idx_b):
        """
        Swap the nodes at the specified indices in the linked list.

        Args:
            idx_a: Index of the first node to swap.
            idx_b: Index of the second node to swap.
        """
        value_a = self.get_by_index(idx_a)
        value_b = self.get_by_index(idx_b)

        curr_node = self.head
        iter_idx = 0
        while curr_node.next:
            if iter_idx == idx_a:
                curr_node.data = value_b
            elif iter_idx == idx_b:
                curr_node.data = value_a
            iter_idx += 1
            curr_node = curr_node.next
        if iter_idx == idx_a:
            curr_node.data = value_b
        elif iter_idx == idx_b:
            curr_node.data = value_a

    def swap_by_value(self, value_a, value_b):
        """
        Swap the nodes containing the specified values in the linked list.

        Args:
            value_a: Value of the first node to swap.
            value_b: Value of the second node to swap.
        """
        idx_a = self.search(value=value_a)
        idx_b = self.search(value=value_b)

        curr_node = self.head
        iter_idx = 0
        while curr_node.next:
            if iter_idx == idx_a:
                curr_node.data = value_b
            elif iter_idx == idx_b:
                curr_node.data = value_a
            iter_idx += 1
            curr_node = curr_node.next
        if iter_idx == idx_a:
            curr_node.data = value_b
        elif iter_idx == idx_b:
            curr_node.data = value_a


if __name__ == '__main__':
    # Example usage of the LinkedList class

    # Create a linked list and append nodes
    ll = LinkedList()
    [ll.append(data=i) for i in range(11)]
    print(ll.travers())

    # Delete nodes by value
    ll.delete(value=3)
    print('Deleted data element: 3')
    print(ll.travers())

    ll.delete(value=6)
    print('Deleted data element: 6')
    ll.delete(value=10)
    print('Deleted data element: 10')
    print(ll.travers())

    # Insert nodes at specific positions
    ll.insert_at(data=-1, index=0)
    print(ll.travers())

    ll.insert_at(data=55, index=5)
    print(ll.travers())

    # Insert at the second last position
    ll_len = ll.size()
    print(f'Before insert at: {ll_len - 1}, LL size is : {ll_len}')
    ll.insert_at(data=99, index=ll_len - 1)
    print(ll.travers())

    # Search for a value
    print('Index of 55 is:', ll.search(value=55))

    # Swap nodes by value and by index
    ll.swap_by_value(value_a=1, value_b=7)
    print('Swapped values 1 and 7:')
    print(ll.travers())

    ll_len = ll.size()
    ll.swap_by_index(idx_a=0, idx_b=ll_len - 1)
    print('Swapped first and last nodes:')
    print(ll.travers())
