class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)
            # only use underscore when working with self (node)
            node.parent = self

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node.parent = None  # see line 18 notes

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if node:
            self._parent = node
            node.add_child(self)

# nodeA = Node("a")
# nodeB = Node("b")
# nodeA.parent = nodeB
#
#
#
# whatever is calling the method is self
