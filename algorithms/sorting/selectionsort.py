def selection_sort(arr, n=None):
    '''
        Procedure SELECTION-SORT(A, n):
        Inputs:
        A: an array.
        n: the number of elements in A to sort.
        Result: The elements of A are sorted into nondecreasing order.

        1. For i = 1 to n - 1:
            A.  Set smallest to i
            B.  For j = i+1 to n:
                    if A[j] < A[smallest], then set smallest to j.
            C.  Swap A[i] with A[smallest]

        Complexity:
        (n-1)+(n-2) + .. . + 1 = n(n+1)/2
        => O(n^2)
    '''
    array_length = len(arr) if n is None else n

    for i in range(array_length - 1):
        smallest = i
        for j in range(i + 1, array_length):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr


if __name__ == '__main__':
    arr = list(map(int, input('Enter space seperated numbers:').split()))
    n = input('Enter number of elements to be sorted, default = all')
    n = None if n == '' else int(n)
    arr = selection_sort(arr, n)
    print('After sorting')
    print(*arr)
