# compare each item to the next
# if out of place swap them

# run times
# worst case - O(n^2)
# average case - O(n^2)
# best case - O(n)
# space complexity -  O(1)

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - 1):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(arr))
