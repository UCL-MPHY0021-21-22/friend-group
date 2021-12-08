def average_age(group):
    all_ages = [person["age"] for person in group.values()]
    return sum(all_ages) / len(group)


def forget(group):
    """Remove the connection between two people."""
    group[person1]["relations"].pop(person2, None)
    group[person2]["relations"].pop(person1, None)


def add_person(group,age,job,relations):
    """Add a new person with the given characteristics to the group."""
    new_person = {
        "age": age,
        "job": job,
        "relations": relations
    }
    group[name] = new_person

if __name__ == "__main__":
    assert len(group) == 4, "Group should have 4 members"
    assert average_age() == 28.75, "Average age of the group is incorrect!"
    assert len(group["Nash"]["relations"]) == 1, "Nash should only have one relation"
    print("All assertions have passed!")
