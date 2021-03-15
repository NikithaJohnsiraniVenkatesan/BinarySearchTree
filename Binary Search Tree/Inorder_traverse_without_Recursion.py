#Inordeer traverse without Recursion
#Using Stack is the obvious way to traverse tree without recursion. 
#Below is an algorithm for traversing binary tree using stack. 

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def PrintInOrder(root):
    current = root
    stack = []
    done = 0
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            print(current.data, end = " ")
            current = current.right
        else:
            break
    print()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

PrintInOrder(root)