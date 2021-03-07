number = int(input("Enter a random number\t"))
divider = int(input("Give me something to divide the number by\t"))

if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")

if number % divider == 0:
    print("Your number divides evenly by " + str(divider))
else:
    print("Your number dosent divide evenly by " + str(divider))