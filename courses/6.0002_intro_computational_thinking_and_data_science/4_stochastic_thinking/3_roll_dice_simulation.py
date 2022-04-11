'''
references:
    Eric Grimson, John Guttag, and Ana Bell. 6.0002 Introduction to Computational Thinking and Data Science. Fall 2016. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu. License: Creative Commons BY-NC-SA. 

Example implementation of stochastic process.
'''
import random

possible_numbers = [1, 2, 3, 4, 5, 6]

def roll_dice_underdetermined():
    return possible_numbers[1]


def roll_dice_stochastic():
    return random.choice(possible_numbers)
    # random.choice() has a uniform distribution = equally probable to choose any number

def test_roll_dice_stochastic(rolls):
    result = ''
    for i in range(rolls):
        result += str(roll_dice_stochastic())
    print(result)

def test_roll_dice_underdetermined(rolls):
    result = ''
    for i in range(rolls):
        result += str(roll_dice_underdetermined())
    print(result)


'''
Given:
    rolls = 5
            
    How probable is it to return "11111"(string of 5 ones)?:
        use DISCRETE PROBABILITY:
            count number of events with property of interest(i.e. are "11111")
            divide by
            all possible events: all possible results of 5 rolls= 6^5
                e.g. 11111, 11112,11115 ... 21342,12342,
        answer = 1/6^rolls = unlikely
'''


def rum_sim(trials, target_text):
    total_occurence = 0
    result = ''
    for t in range(trials):
        print(f'beginning trial {t}')
        for roll in range(len(target_text)):
            result += str(roll_dice_stochastic())
        if(result == target_text):
            total_occurence += 1
        print(f'result = {result}')
        result = ''
        print(f'done with trials {t}')
    return total_occurence

random.seed(0)
def simulate():
    trials = 1000000
    possible_values = 6
    target_text = '11111'
    precision = 8
    total_occurence = rum_sim(trials, target_text)
    print('beginning simulation')
    print(
        f'sample(estimated) probability of {target_text} is {round(total_occurence/trials, precision)}')
    print(
        f'actual probability of {target_text} is {round(1/possible_values**len(target_text), precision)}')


simulate()
