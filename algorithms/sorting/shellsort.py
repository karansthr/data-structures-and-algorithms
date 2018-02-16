def shell_sort(array):
    """
    Shell sort algorithm improves upon the insertion sort by first
    sorting the elements which are certain interval apart and then
    running insertion sort, thereby reducing number of shifting of
    elements.
    """
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            key = array[i]
            j = i
            while j >= gap and key < array[j - gap]:
                array[j] = array[j - gap]
                j = j - gap
            array[j] = key
        gap = gap // 2
    return array


if __name__ == '__main__':
    arr = list(map(int, input('Enter space seperated numbers: ').split()))
    arr = shell_sort(arr)
    print('After sorting')
    print(*arr)
