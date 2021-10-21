"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

class person:

    def __init__(self,name,age,job=''):
        self.name = name
        self.age = age
        self.job = job
        self.relations = {}

    def relationship(self, person2, relationship):
        self.relations[person2] = relationship

def max_age(group):
    ### Takes an input of a list of names in the class "person" and outputs the maximum age in the group ###
    return max([name.age for name in group])

def mean_age(group):
    ### Takes an input of a list of names in the class "person" and outputs the mean age in the group ###
    return sum([name.age for name in group])/len(group)

def max_age_1_relation(group):
    ### Takes an input of a list of names in the class "person" and outputs the max age in the group if they have at least one relation ###
    return max([name.age for name in group if len(name.relations) > 0])

def max_age_1_friend(group):
    ### Takes an input of a list of names in the class "person" and outputs the max age in the group if they have at least one friend ###
    return max([name.age for name in group if list(name.relations.values()).count("friend") >=1])

Jill = person('Jill',26,'Biologist')
Zalika = person('Zalika',28,'Artist')
John = person('John',27,'Writer')
Nash = person('Nash',34,'Chef')
Pete = person('Pete', 52, 'Student')

Jill.relationship('Zalika','friend')
Jill.relationship('John','partner')
Zalika.relationship('Jill','friend')
John.relationship('Jill','partner')
Nash.relationship('John','cousin')
Nash.relationship('Zalika','landlord')

my_group = [Jill,Zalika,John,Nash,Pete]

print(f"Max age: " + str(max_age(my_group)))
print(f"Mean age: " + str(mean_age(my_group)))
print(f"Max age of those that have one or more relations: " + str(max_age_1_relation(my_group)))
print(f"Max age of those that have one or more friends: " + str(max_age_1_friend(my_group)))