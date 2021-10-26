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

def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range") 

a = 0
for i in range(len(group.items())):
    if (a < (group[get_nth_key(group, i)]["age"])):
        a = (group[get_nth_key(group, i)]["age"])
print("The oldest person in the group is aged", a)
print(" ")

b = 0
for i in range(len(group.items())):
    b = len(group[get_nth_key(group, i)]["relations"]) + b
print("The average number of relations per person is",b/len(group.items()))
print(" ")

c = 0
d = 0
for i in range(len(group.items())):
    c = len(group[get_nth_key(group, i)]["relations"])
    if (c >= 1):
        if (d < (group[get_nth_key(group, i)]["age"])):
            d = (group[get_nth_key(group, i)]["age"])
print("The maximum age of a person in the group with at least one relation is",d)
print(" ")