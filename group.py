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



Jill = person('Jill','26','Biologist')
Zalika = person('Zalika','28','Artist')
John = person('John','27','Writer')
Nash = person('Nash','34','Chef')

Jill.relationship(Zalika,'friend')
Jill.relationship(John,'partner')
Zalika.relationship(Jill,'friend')
John.relationship(Jill,'partner')
Nash.relationship(John,'cousin')
Nash.relationship(Zalika,'landlord')

my_group = [Jill,Zalika,John,Nash]


