"""Code By Yukii"""
"""Stretch Goal: Friend group data functions #8"""

def foget(group, person1, person2):
    """it removes the connection between two people in the group"""

    if person1 in group:
        if person2 in group[person1]['relations']:
            del group[person1]['relations'][person2]
    
    if person2 in group:
        if person1 in group[person2]['relations']:
            del group[person2]['relations'][person1]


def add_person(group, name, age, job, relations):
    """it adds a new person with the given characteristics to the group"""

    group[name] = {
        'age': age,
        'job': job,
        'relations': relations
    }


def average_age(group):
    """it calculates the mean age for the group"""

    ages = [properties['age'] for properties in group.values()] 
    return sum(ages)/len(ages)



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
    },

    'Billy': {
        'age': 36,
        'job': 'chef',
        'relations': {}
    }
}

# 3.1
ages = [properties['age'] for properties in my_group.values()]
max_age = max(ages)
print(f"Max age: {max_age}")

# 3.2 
number_of_relations = [len(properties['relations']) for properties in my_group.values()]
mean = sum(number_of_relations)/len(number_of_relations)
print(f"mean # of relations: {mean}")

# 3.3 
age_of_people_with_relations = [properties['age'] for properties in my_group.values() if len(properties['relations']) >=1]
print(f"Max age, with friend: {max(age_of_people_with_relations)}")

# 3.4 
age_of_people_with_friend = [properties['age'] for properties in my_group.values() if 'friend' in properties['relations'].values()]
print(age_of_people_with_friend)