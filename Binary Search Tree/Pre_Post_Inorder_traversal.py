#How do you perform preorder traversal in a given binary tree?
#Preorder, postorder and inorder

#we will see Inoder now(Its traversing from left,root, right)
#Postorder( Left, right, root)
#Preorder(Root, left, right)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)
def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.val),
def printPreOrder(root):
    if root:
        print(root.val),
        printPreOrder(root.left)
        printPreOrder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("The inorder travesal of BST: ",printInorder(root))
print("\n The post order traversal of teh BST is: ",printPostOrder(root))
print("\n The pre ordertraversal of the BST is: ",printPreOrder(root))
        
