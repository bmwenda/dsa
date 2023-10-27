def print_numbers_ascending(n):
    if n != 0:
        print_numbers_ascending(n - 1)
    print(n)


# tail recursion
def print_numbers_descending(n):
    print(n)
    if n != 0:
        print_numbers_descending(n - 1)
