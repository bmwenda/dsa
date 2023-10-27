def reverse_string(string):
    if string == "":
        return ""
    return reverse_string(string[1:]) + string[0]

def palindrome(string):
    """Use two pointers, similar to iterative solution"""
    n = len(string)
    if string == "" or n == 1:
        return True
    if string[0] == string[n - 1]:
        return palindrome(string[1:n - 1])
    return False
