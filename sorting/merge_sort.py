def merge(left_arr, right_arr):
    left_id = 0
    right_id = 0
    sorted_arr = []

    while left_id < len(left_arr) and right_id < len(right_arr):
        if left_arr[left_id] < right_arr[right_id]:
            sorted_arr.append(left_arr[left_id])
            left_id += 1
        else:
            sorted_arr.append(right_arr[right_id])
            right_id += 1

    sorted_arr += left_arr[left_id:]
    sorted_arr += right_arr[right_id:]
    return sorted_arr


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    middle = len(arr) // 2
    arr_left = merge_sort(arr[:middle])
    arr_right = merge_sort(arr[middle:])

    return merge(arr_left, arr_right)


print(merge_sort([12, 3, 2, 7, 9]))
