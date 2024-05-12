def knapsack_max_value(items, capacity):
    values_grid = [[0 for _ in range(capacity)] for _ in range(len(items))]

    for item_id in range(0, len(items)):
        for weight_cells in range(0, capacity):
            item_weight = items[item_id]['weight']
            item_value = items[item_id]['value']
            previous_item_value = values_grid[item_id - 1][weight_cells] if item_id > 0 else 0

            # item would not fit current cells
            if item_weight > (weight_cells + 1):
                values_grid[item_id][weight_cells] = previous_item_value

            # item would fit perfectly
            elif item_weight == (weight_cells + 1):
                values_grid[item_id][weight_cells] = max(previous_item_value, item_value)

            # item would fit + extra cells remaining
            else:
                remaining_cells_value = values_grid[item_id - 1][weight_cells - item_weight] if item_id > 0 else 0
                values_grid[item_id][weight_cells] = max(previous_item_value, item_value + remaining_cells_value)

    return values_grid[len(items) - 1][capacity - 1]


def knapsack_max_value_with_items(items, capacity):
    blank_cell = {'name': '', 'value': 0}
    values_grid = [[blank_cell for _ in range(capacity)] for _ in range(len(items))]

    for item_id in range(0, len(items)):
        for weight_cells in range(0, capacity):
            item = items[item_id]
            previous_item_cell = values_grid[item_id - 1][weight_cells] if item_id > 0 else blank_cell

            # item would not fit current cells
            if item['weight'] > (weight_cells + 1):
                values_grid[item_id][weight_cells] = previous_item_cell

            # item would fit perfectly
            elif item['weight'] == (weight_cells + 1):
                values_grid[item_id][weight_cells] = previous_item_cell if (previous_item_cell['value'] > item['value']) else {'name': item['name'], 'value': item['value']}

            # item would fit + extra cells remaining
            else:
                remaining_cells = values_grid[item_id - 1][weight_cells - item['weight']] if item_id > 0 else blank_cell
                combined_cell = {'name': remaining_cells['name'] + (' ' if len(remaining_cells['name']) else '') + item['name'], 'value': remaining_cells['value'] + item['value']}
                values_grid[item_id][weight_cells] = previous_item_cell if (previous_item_cell['value'] > combined_cell['value']) else combined_cell

    return values_grid[len(items) - 1][capacity - 1]


knapsack_capacity = 6
knapsack_items = [
    {'name': 'water', 'weight': 3, 'value': 10},
    {'name': 'book', 'weight': 1, 'value': 3},
    {'name': 'food', 'weight': 2, 'value': 9},
    {'name': 'jacket', 'weight': 2, 'value': 5},
    {'name': 'camera', 'weight': 1, 'value': 6},
]

result = knapsack_max_value(knapsack_items, knapsack_capacity)
result_full = knapsack_max_value_with_items(knapsack_items, knapsack_capacity)
print(result)
print(result_full)