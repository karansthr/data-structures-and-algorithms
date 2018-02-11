def bubble_sort(arr):
    '''
    PROCEDURE BUBBLESORT(A):
    for i = 1 to A.length-1
        for j = A.length downto i+1
            if A[j] < A[j-1]
                exchange A[j] and A[j+1]
    '''

    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


if __name__ == '__main__':
    arr = list(map(int, input('Enter space seperated numbers:').split()))
    arr = bubble_sort(arr)
    print('After sorting')
    print(*arr)
