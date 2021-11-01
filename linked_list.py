class Node:
    """
    Node with 2 field: data and next
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    """
    Single Linked List data structure
    """
    def __init__(self, head=None):
        self.head = head 

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
