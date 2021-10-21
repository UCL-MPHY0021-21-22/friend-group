"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {"jill": {
                    "age": 26,
                    "occupation": "biologist",
                    "friend": "zalika",
                    "partner": "john",
                    "cousin": "",
                    "landlord": "",
                    "tenant": ""
                                }, 
           "zalika": {
                    "age": 28,
                    "occupation": "artist",
                    "friend": "jill",
                    "partner": "",
                    "cousin": "",
                    "landlord": "nash",
                    "tenant": ""
                     },
           "john": {
                    "age": 27,
                    "occupation": "writer",
                    "friend": "",
                    "partner": "jill",
                    "cousin": "nash",
                    "landlord": "",
                    "tenant": ""
                     },
           "nash": {
                    "age": 34,
                    "occupation": "chef",
                    "friend": "",
                    "partner": "",
                    "cousin": "john",
                    "landlord": "",
                    "tenant": "zalika"}
           
                    }


ages = [my_group[person]["age"] for person in my_group]

# Assuming relations means has partner or cousin
partners = ["partner" for person in my_group if my_group[person]["partner"]]
cousins = ["cousin" for person in my_group if my_group[person]["cousin"]]

relations = []
relations.extend(partners + cousins)

is_related = [my_group[person]["age"] for person in my_group if my_group[person]["partner"] or my_group[person]["cousin"]]

has_friends = [my_group[person]["age"] for person in my_group if my_group[person]["friend"]]

# Print results
print(f"The maximum age in our group is: {max(ages)}")
print(f"The average number of relations among members of the group is: {len(relations)//len(my_group)}")
print(f"The maximum age of the person that has at least one relation is: {max(is_related)}")
print(f"The maximum age of the person that has at least one friend is: {max(has_friends)}")