class Friend:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "name: {}\nage: {}".format(self.name, self.age)

    def get_name(self):
        user_name = input("What is your name - ")
        return "Well hello {}, my name is {}".format(user_name, self.name)


x = Friend("Dudude", "1")

print(x.get_name())
print(x)

