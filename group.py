"""An example of how to represent a group of acquaintances in Python."""

from statistics import mean
import json
import yaml

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

def write_to_json_file(filename, dic):
    f = open(filename,"w")
    text = json.dumps(dic)
    f.write(text)
    f.close()

def read_from_json_file(filename):
    with open(filename, 'r') as f:
        dic = f.read()
        dic = json.loads(dic)
        return dic


def write_to_yaml_file(filename, dic):
    with open(filename, 'w') as f:
        yaml.dump(dic, f)

def read_from_yaml_file(filename):
    with open(filename, 'r') as f:
        dic = yaml.load(f, Loader=yaml.FullLoader)
        return dic



if __name__ == "__main__":
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

    print("Max age:" + max_age(my_group))
    print("Average degree:" + average_degree(my_group))
    print("Max age with one relation:" + max_age_with_one_relation(my_group))
    print("Max age with one friend:" + max_age_with_one_friend(my_group))
    