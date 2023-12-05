# build a tree from given array.
    # Consider array to represent a tree in level order traversal
# convert tree to max heap (to sort ascending)
# start sorting
    # remove root from max heap and swap it with last unsorted element
    # heapify again to maintain valid max heap
    # repeat until root is empty

# time: O(n log n)
# space: O(1)

import heapq

# heap sort using heapq
def heap_sort(arr):
    items = []
    # build a heap by pushing the values into an array
    # we can also just heapify original heapq.heapify(arr)
    for val in arr:
        heapq.heappush(items, val)

    # pop the items from the heap, one by one
    # since every popped item is the smallest, the result is a sorted array
    result = [heapq.heappop(items) for i in range(len(items))]
    return result
