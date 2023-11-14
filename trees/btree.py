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

    while current_node or stack:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        print(current_node.value, end=(" "))
        current_node = current_node.right

def traverse_inorder(root):
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

# time complexity - O(n)
# space complexity - O(h) -> h = height of tree, worst O(n)
def maximum_depth(root):
    if root is None:
        return 0
    return 1 + max(maximum_depth(root.left), maximum_depth(root.right))

# time complexity - O(n)
# space complexity - O(n) -> h = height of tree, worst O(n)
def max_depth_iter(root):
    if root is None:
        return 0
    queue = deque([root])
    levels = 0
    result = []
    while len(queue):
        result.append([])
        # for each level, do the stack update and increment the level count when done
        for i in range(len(queue)):
            current = queue.popleft()
            result[levels].append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        levels += 1
    return result
