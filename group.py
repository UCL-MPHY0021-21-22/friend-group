"""An example of how to represent a group of acquaintances in Python."""

# - Jill is 26, a biologist and she is Zalika's friend and John's partner.
# - Zalika is 28, an artist, and Jill's friend
# - John is 27, a writer, and Jill's partner.
# - Nash is 34, a chef, John's cousin and Zalika's landlord.


my_group = {
    "Jill" : {"age" : 26, "job" : "biologist", 
            "connections" : {"Zalika" : "friend", "John":"partner"}},
    "Zalika" : {"age": 28, "job": "artist",
            "connections" : {"Jill":"friend"}},
    "John" : {"age":27, "job": "writer", "connections":{"Jill":"partner"}},
    "Nash":{"age":34, "job":"chef", "connections":{"John":"cousin", "Zalika":"landlord"}}
}


