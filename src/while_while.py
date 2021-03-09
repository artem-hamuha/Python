i = "g"

x = input("Enter a single digit number - ")

while len(x) > len(i):
    x = input("Error\nTry again - ")
else:
    print("Your lucky number is " + str(round(int(x) / 1.5 * 2)))