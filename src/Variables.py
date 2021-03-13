import sys
import ctypes

x = 10

print(id(x))  # this shows the longer address where the var is stored

print(hex(id(x)))  # this shows a shorter address of where the var is stored

sys.getrefcount(x)  # this increases reference count


def ref_count(address):
    return ctypes.c_long.from_address(address).value


print(ref_count(id(x)))  # this does the same thing as sys but does not increase ref count
