# A class to store a binary tree node
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Function to print all nodes of a given level from left to right
def printGivenLevel(root, level):
 
    # base case
    if root is None:
        return False
 
    if level == 1:
        print(root.key, end=' ')
 
        # return true if at least one node is present at a given level
        return True
 
    left = printGivenLevel(root.left, level - 1)
    right = printGivenLevel(root.right, level - 1)
 
    return left or right
 
 
# Function to print level order traversal of a given binary tree
def printLevelOrderTraversal(root):
 
    # start from level 1 — till the height of the tree
    level = 1
 
    # run till `printGivenLevel()` returns false
    while printGivenLevel(root, level):
        level = level + 1
 
 
if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
 
    printLevelOrderTraversal(root)