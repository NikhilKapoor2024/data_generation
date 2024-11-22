from random import randint

class Die:
    """A class for dice functionality"""

    def __init__(self, num_sides=6):
        """Initialize attributes"""
        self.num_sides = num_sides
    

    def roll(self):
        """Returns random number from 1 to the max"""
        return randint(1, self.num_sides)