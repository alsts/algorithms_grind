def partition(arr, left_id, right_id):
    pivot_value = arr[right_id]  # pick pivot as the end of array
    pivot_id = left_id

    for i in range(left_id, right_id):
        if arr[i] < pivot_value:  # move lower items on left side
            arr[pivot_id], arr[i] = arr[i], arr[pivot_id]
            pivot_id += 1

    # swap pivot(end of array) with item(pivot_id)
    arr[pivot_id], arr[right_id] = arr[right_id], arr[pivot_id]
    return pivot_id


def quick_sort(arr, left_id, right_id):
    if left_id < right_id:
        pivot = partition(arr, left_id, right_id)
        quick_sort(arr, left_id, pivot - 1)
        quick_sort(arr, pivot + 1, right_id)


nums = [12, 3, 2, 7, 9]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
