"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {}

class Group:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)
        

class Person:
    def __init__(self, name, age, jobs, relationships, group = None):
        self.name = name
        self.age = age
        self.jobs = jobs
        self.relationships = relationships
        self.group = group

    def add_job(self, job):
        self.jobs.append(job)

    def add_relationship(self, relationship, name):
        self.relationships[relationship] = name


YLTWH = Group()
Y = Person("Yahya", 24, ["Student"], {})