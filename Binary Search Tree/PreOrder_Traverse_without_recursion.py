#How do you traverse a given binary tree in preorder without recursion?
#Using Stack we are going to trverse a BST iteartively

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def iterativePreOrder(root):
    if root is None:
        return
    nodeStack = []
    nodeStack.append(root)
    
    while(len(nodeStack)>0):
        node = nodeStack.pop()
        print(node.data),
        
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)
root = node(30)
root.left = node(15)
root.right = node(20)
root.left.left =node(10)
root.left.right = node(13)
root.right.left  = node(18)
iterativePreOrder(root)