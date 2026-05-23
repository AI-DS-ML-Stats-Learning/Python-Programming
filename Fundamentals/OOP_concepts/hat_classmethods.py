#using class method now

import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Racvenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)

Hat.sort("Harry")