# Uses python3
import sys
import math


def get_optimal_value(capacity, weights, values):
    cur_cap = capacity
    loot = 0.0
    min_value = min(weights)

    if len(weights) == 1:
        if capacity > weights[0]:
            return values[0]
        else:
            return (capacity / weights[0]) * values[0]

    while cur_cap >= min_value:
        max_value = max(values)
        item_position = values.index(max_value)
        item_weight = weights[item_position]
        max_items = math.floor(cur_cap / item_weight)
        loot += max_items * max_value
        cur_cap = cur_cap - max_items * item_weight
        values.remove(max_value)
    return loot


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
