"""
    References: 
    https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-videos/lecture-1-introduction-and-optimization-problems/
"""

from restuarant import Food, buildMenu
from greedy import greedy

def _test_greedy(menu, constraint, keyFunction):
    taken, total_value = greedy(menu, constraint, keyFunction)
    print(f'Total value of menu items taken: {total_value}')
    print('Items:')
    print(f'name, value, cost')
    for item in taken:
        print(f'{item.name}, {item.getValue()}, {item.getCost()}')


def test_greedys(max_unit):
    foods = ['wine ', 'beer ', 'pizza', 'burger ',
             'fries ', 'coke ', 'apple ', 'donut']
    values = [89, 90, 30, 50, 50, 79, 90, 10]
    calories = [123, 154, 258, 354, 365, 150, 1, 195]

    menu = buildMenu(foods, values, calories)

    print(f'test greedy using {max_unit} calories')
    print('optimising for highest value(maximizing), i.e. highest value items first in sorted order to pick from')
    _test_greedy(menu, max_unit, Food.getValue)

    print()
    print(f'test greedy using {max_unit} cost')
    print('optimising for lowest cost(minimizing), i.e. cheapest cost items first in sorted order to pick from')
    _test_greedy(menu, max_unit, lambda x: 1/Food.getCost(x))

    print()
    print(f'test greedy using {max_unit} value')
    print('optimising for highest density(maximizing), i.e. highest density items first in sorted order to pick from')
    _test_greedy(menu, max_unit, Food.density)


if __name__ == '__main__':
    test_greedys(800)
    print()
