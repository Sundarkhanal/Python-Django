class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' is ' + str(self.age) + ' years old.'

p1 = Person("Sundar", 36)
p1.age = 40
print(p1)
