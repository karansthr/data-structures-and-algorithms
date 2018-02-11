def insertion_sort(arr, n=None):
    '''
    Procedure INSERTION -SORT (A, n)
    Inputs:
        A: array to be sorted
        n: number of elements to be sorted

    1. For i = 2 to n:
    A. Set key to A[i], and set j to i - 1.
    B. While j > 0 and A[j] > key, do the following:
        1.  Set A[j + 1] to A[j].
        2.  Decrement j
    C. Set A[j + 1] to key.
    '''
    array_length = len(arr) if n is None else n
    for i in range(1, array_length):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr


if __name__ == '__main__':
    arr = list(map(int, input('Enter space seperated numbers:').split()))
    n = input('Enter number of elements to be sorted, default = all')
    n = None if n == '' else int(n)
    arr = insertion_sort(arr, n)
    print('After sorting')
    print(*arr)
