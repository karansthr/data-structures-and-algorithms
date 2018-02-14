def bubble_sort_improved(array):
    """
    After every iteration we check the swap flag if the array is already
    sorted then the swap flag will be false after first iteration and
    in that case we can simply return the array.
    """
    size, swap = len(array) - 1, True
    while size > 0 and swap:
        swap = False
        for i in range(size):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True
    return array


array = [1, 5, 3, 7, 2, 0]


print(bubble_sort_improved(array))
