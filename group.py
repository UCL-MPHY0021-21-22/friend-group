"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    'Jill': {
        'age': 26,
        'job': 'biologist',
        'relations': {
            'Zalika': 'friend',
            'John': 'partner'
        }
    },
    
    'Zalika': {
        'age': 28,
        'job': 'artist',
        'relations': {
            'Jill': "friend"
        }
    },

    'John': {
        'age': 27,
        'job': 'writer',
        'relations': {
            'Jill': 'partner'
        }
    },

    'Nash': {
        'age': 34,
        'job': 'chef',
        'relations': {
            'John': "cousin",
            'Zalika': 'landlord'
        }
    }
}


# 3.1
# the maximum age of people in the group
max_age = max([properties['age'] for properties in my_group.values()])
print(f"Max age: {max_age}")

# 3.2 
# the average (mean) number of relations among members of the group
mean_number_of_relations = sum([len(properties['relations']) for properties in my_group.values()]) / len(my_group)
print(f"mean # of relations: {mean_number_of_relations}")

# 3.3 
# the maximum age of people in the group that have at least one relation
age_of_people_with_relations = [properties['age'] for properties in my_group.values() if len(properties['relations']) >=1]
print(f"Max age, with relations: {max(age_of_people_with_relations)}")

# 3.4 
# the maximum age of people in the group that have at least one friend
age_of_people_with_friend = [properties['age'] for properties in my_group.values() if 'friend' in properties['relations'].values()]
print(f"Max age, with friend: {age_of_people_with_friend}")