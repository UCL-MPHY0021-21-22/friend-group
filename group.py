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
    "NewGuyNoFriends": {
        "age": 15,
        "job": "student",
        "relations": {
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

# the maximum age of people in the group
max_age = max([group.get(personName).get("age") for personName in group.keys()])
print("oldest person is", max_age)

# the average (mean) number of relations among members of the group
import numpy as np
relationships_dict_list = [group.get(personName).get("relations") for personName in group.keys()]
mean_relations = np.mean([len(personalRelations.keys()) for personalRelations in relationships_dict_list])
print("mean number of relations is", mean_relations)

# the maximum age of people in the group that have at least one relation
max_nonfriendless = max([group.get(personName).get("age") for personName in group.keys() if len(group.get(personName).get("relations")) != 0])
print("oldest person with at least one friend is", max_nonfriendless, "years old")


# [more advanced] the maximum age of people in the group that have at least one friend




