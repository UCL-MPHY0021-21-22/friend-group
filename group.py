"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
def max_age(group_information):
    max_age = 0
    people = None
    for key, value in group_information.items():
        if max_age < value['age']:
            max_age = value['age']
            people = key

    print("The older people of this group is " + people + " and the age is " + str(max_age))


def mean_num_relation(group_information):
    total = 0

    for key, value in group_information.items():
        length = len(value['connection'])
        total += length
    print("mean of relation is " + str(total // len(group_information)))


def max_age_relation(group_information):
    max_age = 0
    people = ''
    for key, value in group_information.items():
        if max_age < value['age'] and len(value['connection']) > 0:
            max_age = value['age']
            people = key

    print("The older people of this group who has relation is " + people + " and the age is " + str(max_age))


def max_age_friend(group_information):
    max_age = 0
    people = ''
    for key, value in group_information.items():
        if max_age < value['age'] and value['connection']['friend']:
            max_age = value['age']
            people = key

    print("The older people of this group who has at least one friend is " + people + " and the age is " + str(max_age))


def main():
    print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
    my_group = {
        'Jill': {
            'name': 'Jill',
            'age': 26,
            'occupation': 'biologist',
            'connection': {'friend': ['Zalika'], 'partner': ['John'], 'landlord': None, 'relatives': None}
        },
        'Zalika': {
            'name': 'Zalika',
            'age': 28,
            'occupation': 'artist',
            'connection': {'friend': ['Jill'], 'partner': None, 'landlord': ['Nash'], 'relatives': None}
        },
        'John': {
            'name': 'John',
            'age': 27,
            'occupation': 'writer',
            'connection': {'friend': None, 'partner': ['Jill'], 'landlord': None, 'relatives': ['nash(cousin)']}
        },
        'Nash': {
            'name': 'Nash',
            'age': 34,
            'occupation': 'chef',
            'connection': {'friend': None, 'partner': None, 'landlord': None, 'relatives': ['John(cousin)']}
        }
    }
    max_age(my_group)
    mean_num_relation(my_group)
    max_age_relation(my_group)
    max_age_friend(my_group)



if __name__ == '__main__':
    main()

