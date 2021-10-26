"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
def max_age(group_information):
    max_age=0
    people=''
    for key, value in group_information.item():
        if max_age<value:
            max_age=value
            people=key

    print("The older people of this group is "+people+"and the age is "+max_age)

def main():
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
    max_age(my_group)
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")

if __name__=="_main_":
    main()


