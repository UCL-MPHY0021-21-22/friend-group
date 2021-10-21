"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {"Zalika" : {"age" : 28,
                        "job" : "artist",
                        "connection": [ ["Jill", "friend"] ]},
            "Jill" : {"age" : 26,
                      "job" : "biologist",
                      "connection": [ ["Zalika", "friend"], ["John", "partner"]]},
            "John" : {"age" : 27,
                      "job" : "writer",
                      "connection": [ ["Jill", "partner"] ]},
            "Nash" : {"age" : 34,
                      "job" : "chef",
                      "connection": [ ["John", "cousin"], ["Zalika", "landlord"] ]}
}


def forget(group, person1, person2, done_twice=False):
    ''' person1, person2 : str'''
    connection1 = group[person1]["connection"]
    if connection1 == []:
        raise ValueError("Person 1 has no connection")
    else:
        for elem in connection1:
            if elem[0] == person2:
                group[person1]["connection"].remove(elem)
    
    if done_twice is False:
        forget(group,person2,person1,True)

    return(group)
    
def add_person(group, name, age, job, relations):
    group[name] = {"age" : age,
                   "job" : job,
                   "connection":relations}
    return(group)

def average_age(group):
    age_list = []
    for elem in group.values():
        age_list.append(elem["age"])
    return(sum(age_list)/len(age_list))


print(forget(my_group,"Zalika","Nash"))
print(average_age(my_group))
print(add_person(my_group, "Constance", 23, "student", []))