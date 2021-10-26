"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

#my_group = #-JiefuMei-myx2021-thandi1908-SolemnShark871

class Person:
    def __init__(self, name, age, occupation, relationships):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.relationships = relationships  #define relationship

    def add_relationships(self, name, relationships):
        self.relationships = relationships

Jill_relations = {
    "Zalika": "friend",
    "John": "partner"
                     }

Zalika_relations = {
    "Jill":"friend"
}

John_relations = {
    "Jill":"partner"
}

Nash_relations ={
    "John":"cousin",
    "Zalika":"landlord"
}
jill = Person('Jill', 26, "biologist",Jill_relations)
zalika = Person('Zalika',28,"artist",Zalika_relations)
john = Person('John',27,"writer",John_relations)
nash = Person('Nash',34, "chef",Nash_relations)


print(nash.relationships)