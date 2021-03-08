from collections import deque
 
 
# A class to store a binary tree node
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Function to print level order traversal of a given binary tree
def printLevelOrderTraversal(root):
 
    # create an empty queue and enqueue the root node
    queue = deque()
    queue.append(root)
 
    # loop till queue is empty
    while queue:
 
        # process each node in the queue and enqueue their
        # non-empty left and right child
        curr = queue.popleft()
 
        print(curr.key, end=' ')
 
        if curr.left:
            queue.append(curr.left)
 
        if curr.right:
            queue.append(curr.right)
 
 
if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
 
    printLevelOrderTraversal(root)