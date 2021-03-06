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


def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode the digits")
    return ''.join([digit_map[d] for d in digits])


print(encode([15, 15], '0123456789ABCDEF'))


def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError('Invalid base: must be in range of 2 - 36')
    sign = -1 if number < 0 else 1
    number *= sign
    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding


e = rebase_from10(10, 2)  # should get 1010(binary)
print(e)
print(int(e, base=2))  # should get 10
