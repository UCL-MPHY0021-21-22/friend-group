"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

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

#find the biggest age
age_series = []
for name in group['name'] :
    for age in name['age'] :
        age_series.append(age)
#old solution: bubble sort
index = 0
cash = 0
for index in age_series :
    if age_series(index) > age_series(index+1) :
        cash = age_series(index+1)
        age_series(index+1) = age_series(index)
        age_series(index) = cash
    index += 1
print(age_series(len(age_series)-1))
#new solution: max()
#max(age_series)
