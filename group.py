import yaml


"""An example of how to represent a group of acquaintances in Python."""
# Define the group as a series of nested dictionaries

my_group = {'Jill' : 
        {'age' : 26 , 'job' : 'biologist' , 'connections' : 
             {'friend' : 'Zalika' , 'partner' : 'John'}   } , 
            'Zalika' : 
        {'age' : 28 , 'job' : 'artist' , 'connections' : 
             {'friend' : 'Jill' , 'landlord' : 'Nash'}   } , 
            'John' : 
        {'age' : 27 , 'job' : 'writer' , 'connections' : 
             {'partner' : 'Jill' , 'cousin' : 'Nash'}   } , 
            'Nash' : 
        {'age' : 34 , 'job' : 'chef' , 'connections' : 
             {'cousin' : 'John' , 'tenant' : 'Zalika'}   }   }



with open('group_datafile.yaml', 'w') as yaml_file:
    yaml.dump(my_group, yaml_file, default_flow_style=True)


