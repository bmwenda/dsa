"""Reverse array in place
Two pointers technique
"""

# time complexity: O(n)
# space complexity: O(1)
def reverse(arr):
    i = 0
    j = len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

# run time: O(n)
# space complexity O(n)
def is_palindrome(str):
    i = 0
    j = len(str) - 1

    while i < j:
        # skip non alphanumeric characters
        while not str[i].isalnum() and i < j:
            i += 1
        while not str[j].isalnum() and j > i:
            j -= 1

        if str[i].lower() != str[j].lower():
            return False
        i += 1
        j -= 1
    return True
