'''
    references:
        Guttag, John. Introduction to Computation and Programming Using Python: With Application to Understanding Data. 2nd ed. MIT Press, 2016. ISBN: 9780262529624.page 219
'''

class Location():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def new_location(self, x_distance, y_distance):
        return Location(self.x + x_distance, self.y + y_distance)

    def distance_from(self, other):
        x_distance = self.x - other.x
        y_distance = self.y - other.y
        return (x_distance**2 + y_distance**2)**0.5