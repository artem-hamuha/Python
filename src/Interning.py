import sys
import time


def compare_equal(n):
    a = "a very very very very large string" * 200
    b = "a very very very very large string" * 200
    for i in range(n):
        if a == b:
            pass


def compare_interned(n):
    a = sys.intern("a very very very very large string" * 200)
    b = sys.intern("a very very very very large string" * 200)
    for i in range(n):
        if a is b:
            pass


start = time.perf_counter()
print(compare_equal(10000000))
end = time.perf_counter()
print('equality', end-start)

start = time.perf_counter()
print(compare_interned(10000000))
end = time.perf_counter()
print('equality', end-start)
