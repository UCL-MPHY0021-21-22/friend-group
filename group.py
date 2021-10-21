"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    'Jill': {
        'age':26,
        'job':'biologist',
        'connections':{
            'Zalika':'friend',
            'John':'partner'
        }
    },
    'Zalika': {
        'age':28,
        'job':'artist',
        'connections':{
            'Jill':'friend'
        }
    },
    'John': {
        'age':27,
        'job':'writer',
        'connections':{
            'Jill':'partner'
        }
    },
    'Nash': {
        'age':34,
        'job':'chef',
        'connections':{
            'Zalika':'landlord'
        }
    }
}
