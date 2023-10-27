# maintains a sorted sub-array to the left and an unsorted sub-array to the right
    # set minimum value to be at start of left sub-array
    # traverse looking for a value less than current
        # if found, set as new minimum
    # after each run, swap first sub-array item with minimum
    # move to the next array item and set as new minum
    # repeat the steps to find min value and swap

# run times
# worst case - O(n^2)
# average case - O(n^2)
# best case - O(n^2)
# space complexity -  O(1)

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n - 1):
            if (arr[j] < arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(selection_sort(arr))
