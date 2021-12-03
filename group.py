"""Code By Yukii"""
"""Stretch Goal: Friend group data functions #8"""

def forget(group, person1, person2):
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
    }
}


if __name__ == "__main__":
    # test out functions

    # foget
    forget(my_group, 'Jill', "Zalika")
    assert len(my_group['Jill']['relations']) == 1 # Jill should only have one relation

    # add person
    add_person(my_group, 'Bill', 36, 'chef', {})
    assert len(my_group) == 5 #Group should have 5 members

    # average age
    # (26+27+28+34+36) / 5 = 30.2
    assert average_age(my_group) == 30.2

    print('All assertions have passed!')
    
