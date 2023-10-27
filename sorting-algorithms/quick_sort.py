# divide and conquer
# choose a pivot - end of array
# use two pointers i and j to create two sub arrays
# j looks for items greater than pivot and i, items less than pivot
# if j finds an item less than pivot
    # move i to the right: i = i + 1
    # swap the values at index i and j
# do this while i <= j
# if this condition is met
    # swap i + 1 and pivot
    # return index of pivot: i + 1 => pivot_index
# recurse quick_sort function for left and right sub-arrays
    # left args: left = 0, right = pivot_index - 1
    # right args: left = pivot_index + 1, right index = len(arr) - 1

# run times
# worst case - O(n^2) - when array is sorted
# average case - O(n log n)
# best case - O(n log n)
# space complexity -  O(log n)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1 # we need to move to the right after each iteration

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # swap pivot with i + 1
    arr[right], arr[i + 1] = arr[i + 1], arr[right]
    return i + 1

def quick_sort(arr, left, right):
    if left < right:
        partition_index = partition(arr, left, right)
        # process left sub-array
        quick_sort(arr, left, partition_index - 1)
        # process left sub-array
        quick_sort(arr, partition_index + 1, right)

    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(quick_sort(arr, 0, len(arr) - 1))
