import statistics
import yaml

with open('group_datafile.yaml', 'r') as group:
    my_group = yaml.safe_load(group)



# Simple loop to extract ages from the group, and choose the largest

ages = [my_group[a]['age'] for a in my_group]
max_age = max(ages)

print("The oldest person in the group is",max_age,"years old.")


# Find the mean number of relations in the group

num_relations = [len(my_group[a]['connections']) for a in my_group]
mean_number = statistics.mean(num_relations)

print("The mean number of relations amongst the group is",mean_number,"relations.")



# Find the maximum age of people with 1+ relations

ages_connected = [my_group[a]['age'] for a in my_group if len(my_group[a]['connections']) >= 1]
max_age2 = max(ages_connected)

print("The oldest person in the group with at least 1 relation is",max_age2,"years old.")



# Find the maximum age of people with 1+ friends


def has_friends(person):
    if 'friend' in person['connections']:
        friends = person['connections']['friend']
        if isinstance(friends, dict):
            num_friends = len(friends)
        elif isinstance(friends, str):
            num_friends = 1
    else:
        num_friends = 0
    return num_friends


ages_friends = [my_group[a]['age'] for a in my_group if has_friends(my_group[a]) >= 1]
max_age3 = max(ages_friends)

print("The oldest person in the group with at least 1 friend is",max_age3,"years old.")

