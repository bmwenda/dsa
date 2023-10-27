# distribute given input into a suitable number of buckets
# choosing a good number of buckets depends on the case
# key thing is to have good distribution of inputs
# an good option is (max - min) / n
# this is the scatter step
# for each bucket, sort elements using another algorithm like insertion sort
# gather the items again in order
# Applications
    # Top-K queries - finding most frequently occurring element is a dataset
    # External sorting - when dataset doesn't fit into memory and we need to chunk it

# run times - depends on algorithm used to sort bucket items

def sort_bucket_items(arr):
    # insertion sort
    if not len(arr):
        return []
    for i in range(1, len(arr)):
        j = i
        while j > 0:
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
    return arr

def bucket_sort(arr):
    # given input values, 5 bucket seems okay
    bucket = [[] for i in range(5)]

    # distribute
    for num in arr:
        bucket[num // 20].append(num) # [[12, 11], [34, 25, 22], [], [64], [90]]

    # sort items in each bucket
    for items in bucket:
        sort_bucket_items(items) # [[11, 12], [22, 25, 34], [], [64], [90]]

    # gather items
    k = 0
    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1

    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(bucket_sort(arr))
