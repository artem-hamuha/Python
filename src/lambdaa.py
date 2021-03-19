def my_func(n):
    return lambda a, b: a + b - n


my_doubler = my_func(2)
print(my_doubler(11, 3))
