"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

from statistics import mean

my_group = {
        "Jill": { "age": 26,
                "jobs": ["Biologist"],
                "connections": {
                    "friend": ["Zalika"],
                    "partner": ["John"]
                    }
                },
            "Zalika": {
                "age": 28,
                "jobs": ["Artist"],
                "connections": {
                    "friend": ["Jill"]
                    }
            },
            
            "John": {
                "age": 27,
                "jobs": ["Writer"],
                "connections": {
                    "partner": ["Jill"]
                    }
            },
            "Nash": {
                "age": 34,
                "jobs": ["Chef"],
                "connections": {
                    "cousin": ["John"],
                    "landlord": ["Zalika"]   
                }
           }
}


def max_age(group):
    return max([person["age"] for person in list(group.values())])

def num_connections(person):
    return len(person["connections"].keys())

def average_degree(group):
    return mean([num_connections(person) for person in list(group.values())])

def max_age_with_one_relation(group):
    return max([person["age"] for person in list(group.values()) if num_connections(person)])

def max_age_with_one_friend(group):
    return max([person["age"] for person in list(group.values()) if person["connections"].get("friend")])
