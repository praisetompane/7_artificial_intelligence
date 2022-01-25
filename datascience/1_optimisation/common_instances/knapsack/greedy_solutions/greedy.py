"""Performance
    NlogN for sort
    N for iterating through the menu
    O(NlogN) + O(N) = O(NlogN + N) 
    ∴ O(NlogN)
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
