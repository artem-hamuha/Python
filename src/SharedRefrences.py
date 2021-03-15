a = 1000
b = a
c = b

print(id(a) == id(b) == id(c))

print(a is b is c)
