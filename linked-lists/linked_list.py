class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def create_list(n):
    head = Node(1)
    for i in range(2, n + 1):
        append(head, i)
    return head

def append(head, n):
    new_node = Node(n)
    if not head:
        head = new_node
    current = head
    while current and current.next:
        current = current.next
    current.next = new_node
    return head

def append_recursive(head, n):
    if head and head.next is None:
        head.next = Node(n)
        return
    append_recursive(head.next, n)

# time: O(n)
# space: O(1)
def traverse(head):
    current = head
    while current:
        head = current
        print(head.value, end=" ")
        current = current.next

# time: O(n)
# space: O(n)
def traverse_recursive(head):
    if head is None:
        return
    print(head.value, end=" ")
    traverse_recursive(head.next)

def prepend(reversed, new_head):
    new_head.next = reversed
    return new_head

# time complexity: O(n)
# space complexity: O(1)
def reverse_iter(head):
    previous, current = head, None
    while current:
        next_node = current.next
        current.next = previous
        current = next_node
    return previous

# time complexity: O(n)
# space complexity: O(n)
def reverse_recursive(head):
    if not head or not head.next:
        return head
    new_head = reverse_recursive(head.next)
    # make next node point to current node
    head.next.next = head
    # break current next to remove cyclic pointer
    head.next = None
    return new_head

def merge_lists(a, b):
    if a is None:
        return b
    if b is None:
        return a

    if a.value < b.value:
        a.next = merge_lists(a.next, b)
        return a
    else:
        b.next = merge_lists(a, b.next)
        return b
