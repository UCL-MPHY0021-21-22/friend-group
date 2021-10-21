"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
group_info_dic = {
    'Danny': {
        'age':25,
        'job': 'Machine learning engineer',
        'connection': {
            "Juncai": 'Classmate',
            "Jenny": 'Classmate',
            "Cheng Yuan": 'Classmate'
        }
    },
    'Jenny': {
        'age': 21,
        'job': 'Student',
        'connection': {
            "Juncai": 'Classmate',
            "Danny": 'Classmate',
            "Cheng Yuan": 'Classmate'
        }
    },
    'Juncai': {
        'age': 22,
        'job': 'Student',
        'connection': {
            "Danny": "Classmate",
            "Jenny": 'Classmate',
            "Cheng Yuan": 'Classmate'
        }
    },
    'Cheng Yuan': {
        'age': 22,
        'job': 'Student',
        'connection': {
            "Danny": "Classmate",
            "Jenny": 'Classmate',
            "Juncai": 'Classmate'
        }
    }
}
my_group = group_info_dic
