"""An example of how to represent a group of acquaintances in Python."""

class Group:

    # mutual_relationships = {"Landlord": "Tenant", "Tenant": "Landlord", "Friend": "Friend"} # what they are to me: what i am to them

    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)
        person.group = self

    # def mutualize_relationships(self):
    #     for person in self.people:
    #         for relationship in person.relationships.items():
    #             if relationship[1] in self.mutual_relationships.keys():
    #                 try:
    #                     self.people[relationship[0]].relationships[person.name] = self.mutual_relationships[relationship[1]]
    #                 except:
    #                     pass
    
    def hwkq1_max_age(self):
        return max([person.age for person in self.people])

    def hwkq2_mean_num_relationships(self):
        return sum([len(person.relationships) for person in self.people]) / len(self.people)

    def hwkq3_max_age_conditional_relationship(self):
        return max([person.age for person in self.people if len(person.relationships) >= 1])

    def hwkq4_max_age_conditional_friend(self):
        return max([person.age for person in self.people if list(person.relationships.values()).count("Friend") >= 1])

class Person:
    
    def __init__(self, name, age, jobs, relationships, group = None):
        self.name = name
        self.age = age
        self.jobs = jobs
        self.relationships = relationships
        self.group = group

    def add_job(self, job):
        self.jobs.append(job)

    def add_relationship(self, name, relationship):
        self.relationships[name] = relationship


YLTWH = Group()

Jill = Person("Jill", 26, ["Biologist"], {"Zalika": "Friend", "John": "Partner"})
Zalika = Person("Zalika", 28, ["Artist"], {"Jill": "Friend"})
John = Person("John", 27, ["Writer"], {"Jill": "Partner"})
Nash = Person("Nash", 34, ["Chef", "Landlord"], {"John": "Cousin", "Zalika": "Landlord"})

for person in [Jill, Zalika, John, Nash]:
    YLTWH.add_person(person)

# YLTWH.mutualize_relationships()

print("Maximum age of people in the group: {0}".format(YLTWH.hwkq1_max_age()))
print("Mean number of (non-mutualized) relationships in the group: {0}".format(YLTWH.hwkq2_mean_num_relationships()))
print("Max age of people in the group that have at least one relation: {0}".format(YLTWH.hwkq3_max_age_conditional_relationship()))
print("Max age of people in the group that have at least one friend: {0}".format(YLTWH.hwkq4_max_age_conditional_friend()))
