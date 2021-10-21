"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    'Jill':
    {
        'age': 26,
        'job': 'biologist',
        'connection': {'Zalika': 'friend', 'John': 'partner'},
    },
    'Zalika':
    {
        'age': 28,
        'job': 'artist',
        'connection': {'Jill': 'friend'},
    },
    'John':
    {
        'age': 27,
        'job': 'writer',
        'connection': {'Jill': 'partner'},
    },
    'Nash':
    {
        'age': 34,
        'job': 'chef',
        'connection': {'John': 'cousin', 'Zalika': 'landlord'},
    }
}

def forget(person1, person2):
    for name, features in my_group.items():
        if name == person1:
            del features['connection'][person2]
        if name == person2:
            del features['connection'][person1]

def add_person(name, age, job, relations):
    new_features = {'age': age, 'job': job, 'connection': relations}
    my_group[name] = new_features

def average_age():
    cnt = 0
    for name, features in my_group.items():
        cnt += features['age']
    return cnt / len(my_group)

forget('Jill', 'Zalika')
add_person("Jack", 20, 'teacher', {'Zalika': 'landlord'})

print(my_group)
print(average_age())


# Questions:
# 1 Yes
# 2 Yes
# 3 No

