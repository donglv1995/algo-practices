class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if not self.data:
            self.data = data
            return
        
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.insert(data)
                return
            self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
                return
            self.right = Node(data)
    
    def get_min_value(self):
        current = self
        
        while current is not None:
            if current.left is None:
                break
            current = current.left
        return current
    
    def get_max_value(self):
        current = self
        
        while current is not None:
            if current.right is None:
                break
            current = current.right
        return current

def in_order_successor(root: Node, node: Node):
    if node.right is not None:
        return node.right.get_min_value()
    
    successor = Node()

    while root:
        if root.data > node.data:
            successor = root
            root = root.left
        elif root.data < node.data:
            root = root.right
        else:
            break # node found

    return successor
