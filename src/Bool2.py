print(True or True and False, True or (True and False)) #same thing
print((True or True) and False)

a = 10
b = 2

if a/b >= 2:
    print('A is at least 2 times larger than b')

""" This will give you an error
a = 10
b = 0

if a/b > 2:
    print('A is at least 2 times larger than b')
"""

a = 10
b = 0

if b > 0 and a/b >= 2:  # You can do this to prevent it, its just like with booleans
    print('A is at least 2 times larger than b')


if b and a/b >= 2:  # This works too
    print('A is at least 2 times larger than b')
