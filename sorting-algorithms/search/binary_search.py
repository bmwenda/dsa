"""Binary search
 - iterative and recursive solutions
"""

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (end + start) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def b_search_recursive(arr, target):
    left, right = 0, len(arr) - 1
    return search(arr, left, right, target)

def search(arr, left, right, target):
    if left > right:
        return -1
    mid = (left + right) // 2
    if target < arr[mid]:
        return search(arr, left, right - 1, target)
    elif target > arr[mid]:
        return search(arr, left + 1, right, target)
    else:
        return mid
