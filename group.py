"""An example of how to represent a group of acquaintances in Python."""

# - Jill is 26, a biologist and she is Zalika's friend and John's partner.
# - Zalika is 28, an artist, and Jill's friend
# - John is 27, a writer, and Jill's partner.
# - Nash is 34, a chef, John's cousin and Zalika's landlord.


my_group = {
    "Jill" : {"age" : 26, "job" : "biologist", 
            "connections" : {"Zalika" : "friend", "John":"partner"}},
    "Zalika" : {"age": 28, "job": "artist",
            "connections" : {"Jill":"friend"}},
    "John" : {"age":27, "job": "writer", "connections":{"Jill":"partner"}},
    "Nash":{"age":34, "job":"chef", "connections":{"John":"cousin", "Zalika":"landlord"}}
}

#EXERCISES/HOMEWORK
#3.1 
ages = [properties["age"] for name, properties in my_group.items()]
print(f"The max age is {max(ages)}")

#3.2
mean_relationship = [len(properties["connections"]) for properties in my_group.values()]
print(mean_relationship)
print(f"The mean number of the connections is {sum(mean_relationship)/len(mean_relationship)}")

#3.3
ages_new = [properties["age"] for properties in my_group.values() if len(properties["connections"]) >=1]
print(f"now, the max ages is {max(ages_new)}")

#3.4
