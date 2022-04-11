import random
from field import Field
from location import Location
from drunk import UsualDrunk
import matplotlib.pyplot as plt

'''
    SWITCH ON/UNCOMMENT TO GET DETERMINISTIC BEHAVIOUR. FOR TESING
random.seed(0)
'''
'''
    references:
        Guttag, John. Introduction to Computation and Programming Using Python: With Application to Understanding Data. 2nd ed. MIT Press, 2016. ISBN: 9780262529624.page 221
'''


def walk(field, drunk, steps):
    initial_location = field.retrieve_location(drunk)
    for _ in range(steps):
        field.move_drunk(drunk)
    return field.retrieve_location(drunk).distance_from(initial_location)


def simulate_walks(drunk_class, trials, steps):
    distances = []
    trial_drunk = drunk_class()
    origin = Location(0, 0)
    for _ in range(trials):
        field = Field()
        field.add_drunk(trial_drunk, origin)
        distances.append(walk(field, trial_drunk, steps))
    return distances


def drunk_test(drunk_class, trials, walk_lengths):
    for steps in walk_lengths:
        distances = simulate_walks(drunk_class, trials, steps)
        print(
            f'Simulating {drunk_class.__name__} for {trials} trials of {steps} steps')
        print(f'Mean: {round(sum(distances)/len(distances), 4)}')
        print(f'Max: {round(max(distances),2)}')
        print(f'Min: {round(min(distances),2)}')
        print('\n')
        print(f'# distances {trials}')

        plt.scatter(distances, range(trials))
        plt.show()


print('Sanity Checks')
#drunk_test(UsualDrunk, 100, (0, 1))
print('Done Sanity Checks\n')
drunk_test(UsualDrunk, 100, (10, 100, 1000, 10000))
