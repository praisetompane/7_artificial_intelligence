'''
    references:
        Guttag, John. Introduction to Computation and Programming Using Python: With Application to Understanding Data. 2nd ed. MIT Press, 2016. ISBN: 9780262529624.page 219
'''
class Field():
    def __init__(self):
        self.drunks = {}

    def add_drunk(self, drunk, location):
        if drunk not in self.drunks:
            self.drunks[drunk] = location

    def move_drunk(self, drunk):
        if drunk in self.drunks:
            x_distance, y_distance = drunk.take_step()
            current_location = self.drunks[drunk]
            self.drunks[drunk] = current_location.new_location(x_distance, y_distance)

    def retrieve_location(self, drunk):
        return self.drunks[drunk]