"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group ={
      'Jill' : {
         'age':  26,
         'job':  'biologist',
         'relationship':  {'Zalika': 'friend', 'John': 'partner'}
     },
      'Zalika' : {
         'age':  28,
         'job':  'artist',
         'relationship':  {'Jill': 'friend'}
     },
      'John' : {
         'age':  27,
         'job': 'writer',
         'relationship':  {'Jill': 'partner'}
     },
      'Nash'  : {
         'age':  34,
         'job': 'chef',
         'relationship': {'John': 'cousin', 'Zalika': 'landlord' }
     }
}
