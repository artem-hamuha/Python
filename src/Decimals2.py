from decimal import Decimal
import sys
import time

a = 3.1234
b = Decimal('3.1234')
print(sys.getsizeof(a))
print(sys.getsizeof(b))

def run_float(n=1):
    for i in range(n):
        a = 3.1234

def run_decimal(n=1):
    for i in range(n):
        b = Decimal('3.1234')

n = 10000000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print("float - ", end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print("decimal - ", end-start)

def run_float(n=1):
    a = 3.1234
    for i in range(n):
        a + a


def run_decimal(n=1):
    b = Decimal('3.1234')
    for i in range(n):
        b + b


n = 10000000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print("float - ", end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print("decimal - ", end-start)