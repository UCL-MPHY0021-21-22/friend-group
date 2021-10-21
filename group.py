"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
group_info_dic = {
    'Jill': {
        'age':26,
        'job': 'biologist',
        'connection': {
            "Zalika": 'friend',
            "John": 'partner'
        }
    },
    'Zalika': {
        'age': 28,
        'job': 'artist',
        'connection': {
            "Jill": 'friend'
        }
    },
    'John': {
        'age': 27,
        'job': 'writer',
        'connection': {
            "Jill": "partner"
        }
    },
    'Nash': {
        'age': 34,
        'job': 'chef',
        'connection': {
            "John": "cousin",
            "Zalika": 'landlord'
        }
    }
}
my_group = group_info_dic
res = []
for name, info in group_info_dic.items():
    string = '{0:s} is {1:d}, a {2:s}'.format(name,info['age'], info['job'])
    for c_n, c in info['connection'].items():
        string = string + ", and is {0:s}'s {1:s}".format(c_n,c)
    res.append(string)
print(res)


