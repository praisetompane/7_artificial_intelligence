"""
    Source: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-videos/lecture-2-optimization-problems/
"""
class Food:
    def __init__(self, name, value, calories):
        self.name = name
        self.value = value
        self.calories = calories

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return f'{self.name} : {str(self.value)} : {str(self.calories)}'

def buildMenu(food_names, values, calories):
    """food_names,values, calories of same length
       food_names a list of strings
       values and calories list of numbers
       returns list of Foods"""
    menu = []
    for i in range(len(values)):
        menu.append(Food(food_names[i], values[i], calories[i]))
    return menu


def greedy(menu, maxCost, keyFunction):
    """Assumes menu is a list, maxCost >= 0
        keyFunction maps elements of menu to numbers
            keyFunction defines what best means
                used to sort the menu from best to worst
        returns list of foods to order
    """
    menuCopy = sorted(menu, key = keyFunction, reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(menuCopy)):
        if(totalCost + menuCopy[i].getCost() <= maxCost):
            totalCost += menuCopy[i].getCost()
            totalValue += menuCopy[i].getValue()
            result.append(menuCopy[i])
    return (result, totalValue)

    """Performance
        NlogN for sort
        N for iterating through the menu
        O(NlogN) + O(N) = O(NlogN + N) 
        ∴ O(NlogN)
    """

if __name__ == '__main__':
    food, totalValue = greedy()
    print(food)
    print(totalValue)
