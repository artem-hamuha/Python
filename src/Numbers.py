print(bin(10))  # shows binary equal of input
print(bin(5))

print(oct(10))  # octal representation of input

print(hex(255))  # hex representation of input


def from_base10(n, b):
    if b < 2:
        raise ValueError("Base b must be >= 2")
    if n < 0:
        raise ValueError("Number n must be >= 0")
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        m = n % b
        n = n // b
        digits.insert(0, m)
    return digits


print(from_base10(10, 2))

print(from_base10(255, 16))
