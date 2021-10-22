"""An example of how to represent a group of acquaintances in Python."""

# Define the group as a series of nested dictionaries

my_group = {'Jill' : 
        {'age' : 26 , 'job' : 'biologist' , 'connections' : 
             {'friend' : 'Zalika' , 'partner' : 'John'}   } , 
            'Zalika' : 
        {'age' : 28 , 'job' : 'artist' , 'connections' : 
             {'friend' : 'Jill' , 'landlord' : 'Nash'}   } , 
            'John' : 
        {'age' : 27 , 'job' : 'writer' , 'connections' : 
             {'partner' : 'Jill' , 'cousin' : 'Nash'}   } , 
            'Nash' : 
        {'age' : 34 , 'job' : 'chef' , 'connections' : 
             {'cousin' : 'John' , 'tenant' : 'Zalika'}   }   }



# Simple loop to extract ages from the group, and choose the largest

max_age = 0

for a in my_group:
    age = my_group[a]['age']
    if age > max_age:
        max_age = age

print("The oldest person in the group is",max_age,"years old.")


# Find the mean number of relations in the group

num_relations = []

for a in my_group:
    relations = my_group[a]['connections']
    num_relations.append(len(relations))

import statistics
mean_number = statistics.mean(num_relations)

print("The mean number of relations amongst the group is",mean_number,"relations.")



# Find the maximum age of people with 1+ relations

max_age2 = 0

for a in my_group:
    num_relations2 = len(my_group[a]['connections'])
    if num_relations2 >= 1:
        age2 = my_group[a]['age']
        if age2 > max_age2:
            max_age2 = age2

print("The oldest person in the group with at least 1 relation is",max_age2,"years old.")



# Find the maximum age of people with 1+ friends

max_age3 = 0

for a in my_group:
    connections = my_group[a]['connections']
    if "friend" in connections:
        friends = connections['friend']
        if isinstance(friends, dict):
            num_friends = len(friends)
        elif isinstance(friends, str):
            num_friends = 1
        if num_friends >= 1:
            age3 = my_group[a]['age']
            if age3 > max_age3:
                max_age3 = age3

print("The oldest person in the group with at least 1 friend is",max_age3,"years old.")
