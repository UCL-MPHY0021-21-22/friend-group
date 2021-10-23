"""An example of how to represent a group of acquaintances in Python."""
import statistics
# Your code to go here...

my_group = {
    "yinwen":{
        "age":22,
        "job":"student",
        "relationship":{
            "Keru": "friend",
            "Lifeng": "friend"
        }
    },
    "Keru":{
        "age":21,
        "job":"student",
        "relationship":{
            "Yinwen": "partner",
            "Lifeng": "classmate"
        }
    },
    "Lifeng":{
        "age":23,
        "job":"student",
        "relationship":{
            "Yinwen": "friend",
            "Keru": "classmate"
        }
    }
}

# The maximum age of people in the group
list1=[]
for name in my_group:
    list1.append(my_group[name]['age'])
    #print(str(name), my_group[name]['age'])
print("The maximum age of people in the group is", max(list1), "years old")

# The average (mean) number of relations among members of the group
list2=[]
for name in my_group:
    list2.append(len(my_group[name]['relationship']))
average = int (sum(list2)/len(list2))
print("There are", average, "relations among members of the group on average")

# The maximum age of people in the group that have at least one relation
list3=[]
for name in my_group:
    if len(my_group[name]['relationship']) > 1:
        list3.append(my_group[name]['age'])
print("The maximum age of people in the group that have at least one relation is", max(list3), "years old")

# The maximum age of people in the group that have at least one friend
print(max([name['age'] for name in list(my_group.values()) if name["relationship"].get("friend")]))