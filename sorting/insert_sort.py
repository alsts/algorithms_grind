def insertion_sort(arr: [int]):
    for i in range(len(arr)):
        j = int(f'{i}')  # need to copy pointer for swap

        while j > 0 and arr[j] < arr[j - 1]:  # swap if lower than last item
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    return arr


print(insertion_sort([12, 3, 2, 7, 9]))
