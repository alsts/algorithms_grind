def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [i for i in arr if i < pivot]
        right = [i for i in arr if i > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([12, 3, 2, 7, 9]))
