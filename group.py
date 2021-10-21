"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "yinwen":{
        "age":22,
        "job":"student",
        "relationship":{
            "Keru": "partner",
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
        "age":22,
        "job":"student",
        "relationship":{
            "Yinwen": "friend",
            "keru": "classmate"
        }
    }
}