"""Convert a decimal number to binary"""

def decimal_to_binary(n):
    binary = ""
    binary = find_binary(n, n % 2, binary)
    print(binary)

def find_binary(quotient, mod, binary):
    if quotient <= 1:
        return str(quotient)
    quotient = quotient // 2
    return find_binary(quotient, quotient % 2, binary) + str(mod)
