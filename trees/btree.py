# Notes:
# https://www.enjoyalgorithms.com/blog/iterative-binary-tree-traversals-using-stack
# Traversal
# - to understand recursive traversal, it's easier when you implement an iterative approach first
# - DFS traversal uses a stack and BFS uses a queue
# - When doing recursive traversal, each node is visited three times.

from collections import deque

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def insert(root, value):
    # balanced btree
    if root.value > value:
        # add value to the left
        if root.left is None:
            root.left = Node(value)
        else:
            root.left.insert(value)
    else:
        # insert to the right
        if root.right is None:
            root.right = Node(value)
        else:
            root.right.insert(value)

# time complexity - O(n)
# space complexity - O(h) -> h = height of tree
def traverse_preorder_iter(root):
    if root is None:
        return

    stack = [root]
    current_node = root

    while (len(stack) > 0):
        current_node = stack.pop()
        print(current_node.value, end=(" "))
        # insert right child into stack first to give left child priority
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

def traverse_preorder(root):
    print(root.value, end=(" "))
    if root.left:
        traverse_preorder(root.left)
    if root.right:
        traverse_preorder(root.right)

def traverse_inorder_iter(root):
    if root is None:
        return

    stack = []
    current_node = root

    while (len(stack) > 0) or current_node is not None:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        print(current_node.value, end=(" "))
        current_node = current_node.right

def traverse_inorder(root):
    # traverse inorder
    if root.left:
        traverse_inorder(root.left)
    print(root.value, end=(" "))
    if root.right:
        traverse_inorder(root.right)

def traverse_postorder(root):
    if root.left:
        root.left.traverse_postorder()
    if root.right:
        root.right.traverse_postorder()
    print(root.value, end=(" "))

def breadth_first_search(root):
    # builtin queue optimised for removing items at index 0
    queue = deque()
    queue.append(root)
    current_node = root

    while len(queue):
        current_node = queue.popleft()
        print(current_node.value, end=" ")
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    # traverse_preorder_iter(root)
    # traverse_preorder(root)

    # traverse_inorder(root)
    # traverse_inorder_iter(root)

    # traverse_postorder(root)
    breadth_first_search(root)
