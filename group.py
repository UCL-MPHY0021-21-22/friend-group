group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}


# Add some code that makes use of comprehension expressions to your group.py file so that it prints out the following when the script is run:

# the maximum age of people in the group
max_age = max([group.get(personName).get("age") for personName in group.keys()])


# the average (mean) number of relations among members of the group
import numpy as np
mean_relations = np.mean([len(personalRelations.keys()) for personalRelations in relationships_dict_list])

# the maximum age of people in the group that have at least one relation
# [more advanced] the maximum age of people in the group that have at least one friend