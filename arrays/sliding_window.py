"""Sliding window
Reduces nested loops when the computational size is fixed
General use case is any operation that considers a part of a larger set, eg subarrays, substrings, etc
Applications:
 - finding duplicates
 - max/min sum
 - finding if a string is a substring
 - etc
"""

# Given an array of integers and a target k, determine if there are duplicates within indices i and j where j - i <= k
def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    start, end = 0, 0
    unique = set()
    while end < len(nums):
        if nums[end] in unique:
            return True
        if end - start >= k: # window size
            unique.remove(nums[start]) # keep reference size constant
            start += 1 # slide window left
        unique.add(nums[end])
        end += 1
    return False


# Given an array of integers and a target k, determine the shortest length of a subarray whose sum >= target
def min_sub_array_len(nums: list[int], target: int) -> int:
    shortest_length = float('inf') # or math.inf
    running_sum = 0
    start, end = 0, 0
    while end < len(nums):
        running_sum += nums[end]
        while running_sum >= target:
            # len of array is (last index - first index) + 1
            shortest_length = min(shortest_length, (end - start) + 1)
            running_sum -= nums[start]
            start += 1
        end += 1
    return shortest_length
