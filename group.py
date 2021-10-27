"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {"Jill": {"age": 26, "job": "biologist", "relations": {"Zalika": "friend", "John": "partner"}},"Zalika": {"age": 28, "job": "artist", "relations": {"Jill": "friend"}}, "John": {"age": 27, "job": "writer", "relations": {"Jill": "partner"}}, "Nash": {"age": 34, "job": "chef", "relations": {"John": "cousin", "Zalika": "landlord"}}}

print(max({name: room['age'] for name, room in my_group.items()}.values()))

import statistics as sts

print(sts.mean({name: len(room['relations']) for name, room in my_group.items()}.values()))

print(max({name: room['age'] for name, room in my_group.items() if len(room['relations'])>0}.values()))