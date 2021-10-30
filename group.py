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
    },
    "Peter":{
        "age": 25,
        "job": "photographer",
        "relations":{

        }
    }
}

#HOMEWORK: list comprehension
print("Results for homework:")
#————————————————find the max age————————————————
hw_age_series = [hw_information['age'] for hw_name,hw_information in group.items()]
print("The maximum age is",max(hw_age_series))

#————————————————find the average number of relations————————————————
hw_relations_num_series = [len(hw_information['relations'].values()) for hw_name,hw_information in group.items()]
sum = 0
for number in hw_relations_num_series:
    sum = sum + number
hw_mean = sum/len(hw_relations_num_series)
print("The average number of relations is",hw_mean)

#————————————————find the max age of people in the group that have at least one relation————————————————
hw_age_seires_people_have_relations = [hw_information['age'] for hw_name,hw_information in group.items() if len(hw_information['relations'].values()) != 0]
print("The maximum age of people in the group that have at least one relation is", max(hw_age_seires_people_have_relations))

#————————————————find the max age of people in the group that have at least one friend————————————————
hw_age_series_people_have_friend = [hw_information['age'] for hw_name, hw_information in group.items() if ('friend' in hw_information['relations'].values()) ]
print("The maximum age of people in the group that have at least one friend is", max(hw_age_series_people_have_friend))




#PRACTISE: building lists with append
print("\nResults of practice of normal iterate:")
#————————————————find the max age————————————————
age_series = []
for name,information in group.items():
        age_series.append(information['age'])
#print(age_series)
#old solution: "partial" bubble sort
'''index = 0
temp_age = 0
for index in range(len(age_series)):
    if index >= 3:
        break
    elif  age_series[index] > age_series[index+1]:
        temp_age = age_series[index+1]
        age_series[index+1] = age_series[index]
        age_series[index] = temp_age
        index += 1
    elif age_series[index] <= age_series[index+1]:
        index += 1
print("the maximum age is",age_series[len(age_series)-1])'''
#new solution: max()
print("The maximum age is",max(age_series))

#————————————————find the average number of relations————————————————
relations_num_series = []
sum = 0
for name,information in group.items():
    relations_num_series.append(len(information['relations'].values()))
for number in relations_num_series:
    sum = sum + number
mean = sum/len(relations_num_series)
print("The average number of relations is",mean)

#————————————————find the max age of people in the group that have at least one relation————————————————
age_seires_people_have_relations = [] 
for name,information in group.items():
    if len(information['relations'].values()) != 0:
        age_seires_people_have_relations.append(information['age'])
print("The maximum age of people in the group that have at least one relation is", max(age_seires_people_have_relations))

#————————————————find the max age of people in the group that have at least one friend————————————————
age_series_people_have_friend = []
for name, information in group.items():
    if ('friend' in information['relations'].values()):
        age_series_people_have_friend.append(information['age'])
print("The maximum age of people in the group that have at least one friend is", max(age_series_people_have_friend))
