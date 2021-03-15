#How do you traverse a binary tree in postorder traversal without recursion?

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def PostOrder(head):
    temp = head
    visited = set()
    while (temp and temp not in visited):
        if (temp.left and temp.left not in visited):
            temp = temp.left
        elif  (temp.right and temp.right not in visited):
            temp = temp.right
        else:
            print(temp.data, end = " ")
            visited.add(temp)
            temp = head

if __name__ == "__main__":
    root = node(8)
    root.left = node(3)
    root.right = node(5)
    root.left.left = node(8)
    root.left.right = node(7)
    root.left.right.left = node(18)
    root.left.right.right = node(7)
    root.right.right = node(34)
    PostOrder(root)