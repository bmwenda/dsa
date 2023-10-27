class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

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

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    r = reverse_recursive(head)
    traverse(r)
    # reverse_iter(head)
