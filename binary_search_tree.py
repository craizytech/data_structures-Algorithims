class Node:
    """This creates a node structure"""
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = g
c.right = f

