import time


def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1, n+1):
        s = s + i
    end_time = time.time()
    return end_time-start_time


x = 10000000
print("\nTime to sum of 1 to", x, "and required time to calculate is :", sum_of_n_numbers(x))
