"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

# my_group = Jiayi21-JiefuMei-myx2021-thandi1908-SolemnShark871

class Person:
    def _init_(self, name, age, occupation ):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.relationships = {}  #define relationship

    #def add_relationships(self, name, relationships):
        


Jill_relations = {"Zalika": "friend", "John": "partner"}


#Homework: Extension
#TODO: 
#Add some code that makes use of comprehension expressions to your group.py file so that it prints out the following when the script is run:

# 1. the maximum age of people in the group
# 2. the average (mean) number of relations among members of the group
# 3. the maximum age of people in the group that have at least one relation
# 4. [more advanced] the maximum age of people in the group that have at least one friend

# Let's use the dictionary approach for this 

group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}

#1. The maximum age of people in the group 

max_age = max([group[person]["age"] for person in group])
print(max_age)

#2. The mean number of relationships for people in the group

import numpy as np
#average of a list of the number of relationships for all the people in group
av_rels = np.mean([len(group[person]["relations"]) for person in group])

print(av_rels)

#3 Maximum age of people in the group who have at least one relation

group_w_rels = { } #create a new group for people with relations


for person in group:
    if len(group[person]["relations"]) > 0:
        group_w_rels[person] = group[person]

#max age of person in group of people with relations
max_age_rels = max( 
    group_w_rels[person]["age"] for person in group_w_rels 
)
print(max_age_rels)

# 4 [more advanced] the maximum age of people in the group that have at least one friend

group_w_friends = { }

for person in group:
    if "friend" in group[person]["relations"].values():
        group_w_friends[person] = group[person]

max_age_friends = max( 
    group_w_friends[person]["age"] for person in group_w_friends 
)

print(max_age_friends)


