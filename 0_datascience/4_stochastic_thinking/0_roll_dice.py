'''
references:
    Eric Grimson, John Guttag, and Ana Bell. 6.0002 Introduction to Computational Thinking and Data Science. Fall 2016. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu. License: Creative Commons BY-NC-SA. 

Example implementation of stochastic process.
'''
import random

possible_numbers=[1,2,3,4,5,6]

def roll_dice_underdetermined():
    return possible_numbers[1]

def roll_dice_stochastic():
    return random.choice(possible_numbers)

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

#random.choice() has a uniform distribution = equally probable to choose any number

'''
Given:
    rolls = 5
            
    How probable is it to return "11111"(string of 5 ones)?:
        use DISCRETE PROBABILITY:
            count number of events with property of interest(i.e. are "11111")
            divide by
            all possible events: all possible results of 5 rolls= 6^5
                e.g. 11111, 11112,11115 ... 21342,12342,
        answer = 1/6^5 = unlikely
'''