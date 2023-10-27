# maintains a sorted sub-array to the left and an unsorted sub-array to the right
# need to insert first value in the unsorted sub-array to it's correct place in the sorted sub-array
# for the first iteration, sorted sub-array has first item sorted
# start outer loop at index 1 (second array item, also first item in unsorted sub-array)
# iterate the left sub-array from right to left
    # compare current item with the left item in the sorted sub-array
            # if left is greater than right, swap them
        # move to next array item and repeat

# run times
# worst case - O(n^2)
# average case - O(n^2)
# best case - O(n)
# space complexity -  O(1)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(insertion_sort(arr))
