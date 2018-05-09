class InitialObj:
    def __init__(self, name, places):
        self.name = name
        self.places = places

    def __repr__(self):
        return "\r\nname: %s >> places:%s" % (self.name, self.places)


class FinalObj:
    def __init__(self, names, place):
        self.names = names
        self.place = place

    def __repr__(self):
        return "\r\nplace: %s >> names:%s" % (self.place, self.names)


test_array = [
    InitialObj("Group1", ["Oradea", "Paris", "Budapest", "Bucharest"]),
    InitialObj("Group2", ["Oradea", "Paris"]),
    InitialObj("Group2", ["Paris", "London"]),
    InitialObj("Group3", ["Budapest", "Bucharest"])
]


def the_function(initial_array):
    final_dictionary = {}
    final_array = []

    for initial_object in initial_array:
        for location in initial_object.places:
            if location in final_dictionary:
                if initial_object.name not in final_dictionary[location]:
                    final_dictionary[location].append(initial_object.name)
            else:
                final_dictionary[location] = [initial_object.name]

    for place, names in final_dictionary.items():
        final_array.append(FinalObj(names, place))

    return final_array


print("Initial:")
print(test_array)
print("Final:")
print(the_function(test_array))
