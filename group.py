"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

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
                "jobs": ["Artist"]},
                "connections": {
                    "friend": ["Jill"]
                    }
            "John": {
                "age": 27,
                "jobs": ["Writer"]},
                "connections": {
                    "partner": ["Jill"]
                    }
            "Nash": {
                "age": 34,
                "jobs": ["Chef"],
                "connections": {
                    {
                    "cousin": ["John"],
                    "landlord": ["Zalika"]
                    }
                }
        }
