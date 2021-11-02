class Node:
    """
    Node with 2 field: data and next
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class CircularLinkedList:
    """
    Single Circular Linked List data structure
    """

    def __init__(self, nodes=None):
        """
        Creating Circular Linked List with given elements in nodes.
        Nodes parameter can be any iterable object.
        Time complexity: O(n)
        """
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next
            node.next = self.head

    def __repr__(self):
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if self.head is not None:
            nodes = ""
            for current_node in self:
                nodes += f"{str(current_node.data)} -> "
            return f"{self.__class__.__name__}: {nodes}head({self.head.data})"
        return "None"

    def __iter__(self):
        """
        Each iteration will take constant time and space complexity
        """
        if self.head is None:
            return 0
        yield self.head
        node = self.head.next
        while node is not self.head:
            yield node
            node = node.next

    def __len__(self):
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        count = 0
        for current_node in self:
            count += 1
        return count

    def add_first(self, data):
        """
        Insertion node with data parameter at the beginning of
        Circular Linked List.
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.head is not None:
            self.add_between(1, data)
            temp = self.head.data
            self.head.data = data
            self.head.next.data = temp
        else:
            self.head = Node(data)
            self.head.next = self.head

    def add_last(self, data):
        """
        Insertion node with data parameter at the end of Circular Linked List.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        node = Node(data)
        if self.head is None:
            self.add_first(data)
        else:
            for current_node in self:
                pass
            current_node.next = node
            node.next = self.head

    def add_between(self, position, data):
        """
        Insert node in given position. Insertion is similiar to the
        logic of list.insert()
        Time complexity: O(n)
        Space complexity: O(1)
        """
        node = Node(data)
        length_of_linked_list = len(self)
        if position >= length_of_linked_list:
            self.add_last(data)
            return
        elif position == 0 or (
            position < 0 and abs(position) >= length_of_linked_list
        ):  # noqa: E501
            self.add_first(data)
            return
        count = 0
        for current_node in self:
            if count == length_of_linked_list - abs(position) - 1:
                break
            count += 1
        node.next = current_node.next
        current_node.next = node

    def remove_first(self):
        """
        Remove first node.
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.head is None:
            raise Exception("Circular Linked List is empty!")
        self.head.data = self.head.next.data
        self.head.next = self.head.next.next

    def remove(self, data):
        """
        Remove node with given data. Raises Exception if
        Circular Linked List is empty or node with given data not found
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if self.head is None:
            raise Exception("Circular Linked List is empty!")
        if self.head.data == data:
            if self.head.next == self.head:
                self.head = None
            else:
                self.remove_first()
            return
        prev_node = self.head
        for current_node in self:
            if current_node.data == data:
                prev_node.next = current_node.next
                return
            prev_node = current_node
        raise Exception(f"Node with {data} not found!")
