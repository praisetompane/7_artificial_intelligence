import random
'''
    references:
        Guttag, John. Introduction to Computation and Programming Using Python: With Application to Understanding Data. 2nd ed. MIT Press, 2016. ISBN: 9780262529624.page 220
'''
class Drunk():
    def __init__(self, name=None):
        self.name = name


class UsualDrunk(Drunk):
    def take_step(self):
        steps_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(steps_choices)
