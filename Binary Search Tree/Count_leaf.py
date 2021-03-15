#How do you count a number of leaf nodes in a given binary tree? 

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def getLeafcounts(node):
    if node is None:
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return getLeafcounts(node.left) + getLeafcounts(node.right)
    
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

print("Leaf count of the tree is ", (getLeafcounts(root)))