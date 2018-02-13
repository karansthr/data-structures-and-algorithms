def bubble_sort_improved(array):
    """
    After every iteration we check the swap flag if the array is already
    sorted then the swap flag will be false after first iteration and
    in that case we can simply return the array.
    """
    size, swap = len(array) - 1, True
    for i in range(size):
        if not swap:
            return array
        for j in range(size - i):
            swap = False
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = True
    return array


array = [1, 5, 3, 7, 2, 0]


print(bubble_sort_improved(array))
