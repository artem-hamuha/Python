import random


def generator():
    num1 = int(input("Enter a any number - "))
    num2 = int(input("Enter a second number - "))

    if num1 < num2:
        print(random.randint(num1, num2))
    else:
        print(random.randint(num2, num1))


print(generator())