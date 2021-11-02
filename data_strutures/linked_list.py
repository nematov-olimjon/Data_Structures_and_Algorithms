class Node:
    """
    Node with 2 field: data and next
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    """
    Single Linked List data structure
    """

    def __init__(self, nodes=None):
        """
        Creating Linked List with given elements in nodes.
        Nodes parameter can be any iterable object.
        """
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        count = 0
        for current_node in self:
            count += 1
        return count

    def add_first(self, data):
        """
        Insertion node with data parameter at the beginning of Linked List.
        """
        node = Node(data)
        node.next = self.head
        self.head = node

    def add_last(self, data):
        """
        Insertion node with data parameter at the end of Linked List.
        """
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            for current_node in self:
                pass
            current_node.next = node

    def add_between(self, position, data):
        """
        Insert node in given position. Insertion is similiar to the
        logic of list.insert()
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
            if count == abs(position) - 1:
                break
            count += 1
        node.next = current_node.next
        current_node.next = node

    def remove(self, data):
        """
        Remove node with given data. Raises Exception if
        Linked List is empty or node with given data not found
        """
        if self.head is None:
            raise Exception("Linked List is empty!")
        if self.head.data == data:
            self.head = self.head.next
            return

        prev_node = self.head
        for current_node in self:
            if current_node.data == data:
                prev_node.next = current_node.next
                return
            prev_node = current_node
        raise Exception(f"Node with {data} not found!")
