"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    'Jill':{
        'name':'Jill',
        'age':'26',
        'occupation':'biologist',
        'connection':{'friend':['Zalika'],'partner':['John'],'landlord':None,'relatives':None}
    },
    'Zalika':{
        'name':'Zalika',
        'age':'28',
        'occupation':'artist',
        'connection':{'friend':['Jill'],'partner':None,'landlord':['Nash'],'relatives':None}
    },
    'John':{
        'name':'John',
        'age' :'27',
        'occupation':'writer',
        'connection':{'friend':None,'partner':['Jill'],'landlord':None,'relatives':['nash(cousin)']}
    },
    'Nash':{
        'name':'Nash',
        'age':'34',
        'occupation':'chef',
        'connection':{'friend':None,'partner':None,'landlord':None,'relatives':['John(cousin)']}
    },
}

