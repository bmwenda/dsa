"""A monotonic stack maintains an order
https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems
Applications:
    decreasing monotonic stack:
     - next greater element NGE)
     - previous greater element
     - longest increasing subsequence
     - largest rectangle histogram

    increasing monotonic stack:
     - next smallest element (NSE)
     - previous greater element
     - longest decreasing subsequence
"""

def increasing_monotonic(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
    return stack


def decreasing_monotonic(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
    return stack
