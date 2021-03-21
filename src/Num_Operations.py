num = 3.5
num2 = 3.4

print(round(num), ",", round(num2))  # this works well

num = 3.5678153
num2 = 3.4357689

print(round(num, 2), ",", round(num2, 2))  # you can also use round() to round from any decimal place

print(abs(3))  # abs stands for absolute value
print(abs(-5))  # it always returns a positive

print(pow(3, 2))  # this says three to the power of two
# pow means power as if raise to the power of

num = 8
num2 = 5

print(divmod(num, num2))  # divmod floors what you pass in and mods it
print(num // num2, ",", num % num2)  # like this

import math

print(math.trunc(num))
num = 4.5
print(math.trunc(num))  # trunc truncate the variable you pass through it
num = 4.99999
print(math.trunc(num))

print(math.floor(num))  # floor basically rounds the number down forcefully
print(math.ceil(num))  # ceil basically rounds the number up forcefully


