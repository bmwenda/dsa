# divide array into two sub arrays recursively
# at the last call, we have sub arrays of length 1, hence sorted
# start merging back
    # if left item is less than right item, insert left item to left most available index of array
    # else: insert right item at left most available index
# during this process, some sub-arrays may be empty
# hence do above condition while left or right sub arrays are not empy
# consider empty cases
# if left subarray is empty
    # insert right item to main array
# if right sub array is empty
    # insert left item to main array

# run times
# worst case - O(n log n)
# average case - O(n log n)
# best case - O(n log n)
# space complexity -  O(n)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # integer division
        left_array = arr[:mid]
        right_array = arr[mid:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1

        # consider left over items in sub arrays.
        # right array became empty and we have items in left array
        # merge them into main array
        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1

        # left array became empty and we have items in right array
        # merge each to main array
        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(merge_sort(arr))
