"""Performance
    NlogN for sort
    N for iterating through the menu
    O(NlogN) + O(N) = O(NlogN + N) 
    ∴ O(NlogN)

    items = items available to choose from
    constraint = constraint(s)
    keyFunction(i.e. optimisation function) = what we are optimising for,
                                              encoded in a value which results in the most desired items positioned to the 
                                              far right/futher down in an ascending order sort.
                                                i.e. They have the "biggest" value for the crierion we are optimising for.
                                                NB: It is for this reason, that we reverse the sorted items. 
                                                This is so that the greedy algorithm can correctly take from the most to the least desired/valuable of the items IN ORDER.
                                            For maximising = use the actual optimisation value
                                            For minimizing = use the 1/optimisation value
"""


def greedy(items, constraint, keyFunction):
    items_selected = []
    total_cost, total_value_acquired = 0, 0
    items_sorted = sorted(items, key=keyFunction, reverse=True)

    for item in items_sorted:
        if total_cost + item.getCost() <= constraint:
            items_selected.append(item)
            total_cost += item.getCost()
            total_value_acquired += item.getValue()
    return (items_selected, total_value_acquired)
