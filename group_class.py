# Same exercise using CLASS method

class Person:

    def __init__(self, name, age, job, relationship):
        self.name = name
        self.age = age
        self.job = job
        self.relationship = relationship


person1 = Person("Jill", 26, "biologist", {"Zalika":"Friend", "John":"Partner"})
person2 = Person("Zalika", 28, "artist", {"Jill":"Friend"})

my_group_class = {"Jill":person1,
                   "Zalika":person2}

print(my_group_class["Jill"])


