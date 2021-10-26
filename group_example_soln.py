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

def max_age(group):
    """ Finds the maximum age of a group of people.
    """
    ages = []
    for i in range(len(group)):
        vals = list(group.values())[i]
        ages.append(vals["age"])
    return max(ages)

def mean_num_relations(group):
    """ Finds the average number of relations amongst each member 
    of a group of people.
    """
    tot_relations = 0
    for i in range(len(group)):
        tot_relations += len(list(group.values())[i]["relations"])
    return tot_relations/len(group)

def max_age_w_rel(group):
    """Finds, within a group of people, the maximum age amongst 
    the subgroup of people who have at least one relation to 
    another member of the group.
    """
    ages = []
    for i in range(len(group)):
        if len(list(group.values())[i]["relations"]) > 0:
            ages.append(list(group.values())[i]["age"])
    return max(ages)


def max_age_w_friend(group):
    """ Finds the age of the oldest person in the group who is 
    also friends with someone else in the group.
    """
    ages = []
    for i in range(len(group)):
        relations = list(group.values())[i]["relations"].values()
        if 'friend' in relations:
            ages.append(list(group.values())[i]["age"])
    return  max(ages)

oldest_person_age = max_age(group)
print("The oldest person is in the group is", oldest_person_age,"years old!")

mean_rels = mean_num_relations(group)
print("The mean number of relations that exist between the group members is", mean_rels)

max_age_with_relation = max_age_w_rel(group)
print("The maximum age amongst the people that have at least one relation to another member of the group is", max_age_with_relation)


max_age_with_friend = max_age_w_friend(group)
print("The maximum age amongst those that are friends with someone else in the group is", max_age_with_friend)