class PersonData:
    def __init__(self, name, age, occupation,connections):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.connections = connections
        
    
jill = PersonData('Jill',26,'Biologist',{'Friend':['Zalika'],'Partner':['John']})    
zalika = PersonData('Zalika', 28, 'Artist', {'Friend':['Jill']})
john = PersonData('John',27,'Writer',{'Partner':['Jill']})
nash = PersonData('Nash',34,'Chef',{'Cousin':['John'],'Landlord':['Zalika']})

friendGroup = {
        'Jill': jill,
        'Zalika': zalika,
        'John': john,
        'Nash': nash,
        }

print(friendGroup['John'].connections)