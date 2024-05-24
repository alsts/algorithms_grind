def find_min_id(arr):
    min_id = 0

    for i in range(len(arr)):
        if arr[i] < arr[min_id]:
            min_id = i

    return min_id


def selection_sort(arr):
    sorted_arr = []

    while len(arr) > 0:
        min_id = find_min_id(arr)
        sorted_arr.append(arr.pop(min_id))

    return sorted_arr


print(selection_sort([12, 3, 2, 7, 9]))
