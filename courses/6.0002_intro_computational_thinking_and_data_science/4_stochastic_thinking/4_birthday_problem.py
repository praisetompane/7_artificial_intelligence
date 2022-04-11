'''
    What is the probability of people sharing a birthday?

    Given
        367 people
    Then
        p = 1
        by way of pigeon hole principle
            i.e. There are 367 people(birthdays) and ONLY 366 holes(dates)
                ∴ 2 people WILL HAVE TO share a hole(birthday)

    Analytic Solution:
        Assumption: Each birthday is EQUALLY LIKELY
                366!
        1 - ---------------
            366ᴺ * (366-N)!

'''
from math import factorial
import random

year_days = 366

random.seed(0)

def exists_people_with_same_birthday(total_people, number_people_sharing_birthday):
    '''
        total_people = population size
        number_people_sharing_birthday = number of people sharing a birthday we are testing for.
    '''

    birthdays_count = [0]*year_days
    possible_dates = range(year_days)
    for _ in range(total_people):
        birthday = random.choice(possible_dates)
        birthdays_count[birthday] += 1
    return max(birthdays_count) >= number_people_sharing_birthday


def same_birthday_probability(total_people, trials, number_people_sharing_birthday):
    total_birthdays_shared = 0
    for _ in range(trials):
        if exists_people_with_same_birthday(total_people, number_people_sharing_birthday):
            total_birthdays_shared += 1

    return total_birthdays_shared/trials

def simulate():
    for total_people in [10, 20, 40, 100]:
        trials = 10000
        num_people_shared_birthday = 2

        numerator = factorial(year_days)
        denominator = year_days**total_people * factorial(year_days-total_people)

        print(f'actual probability of {num_people_shared_birthday} in {total_people} people sharing: {1 - (numerator/denominator)}')
        print(f'sampled probability of {num_people_shared_birthday} in {total_people} people sharing: {same_birthday_probability(total_people, trials, num_people_shared_birthday)}')

simulate()

'''
        Simulation vs Analytic Method
            Simulation:
                - Easier to update to another number of people
                - Easier to update distribution of birthdays(i.e. likelihood of each birthday)
            Analytic:
                - Very hard to update to another number of people
                - Very hard to update distribution of birthdays(i.e. likelihood of each birthday)

        
'''