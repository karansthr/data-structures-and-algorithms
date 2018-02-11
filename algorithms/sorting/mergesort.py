def merge(arr, start, middle, end):
    # merge two array
    # first : arr [ start to middle ]
    # second : arr [ middle + 1 to end ]

    A = arr[start:middle + 1]
    B = arr[middle + 1:end + 1]

    i = j = 0
    for k in range(start, end + 1):
        if i <= middle-start and j <= end-middle-1:
            if A[i] <= B[j]:
                arr[k] = A[i]
                i = i + 1
            else:
                arr[k] = B[j]
                j = j + 1
        else:
            if i > middle:
                arr[k] = B[j]
                j = j + 1
            else:
                arr[k] = A[i]
                i = i + 1
    return arr


def mergesort(arr, start, end):
    if start >= end:
        # in this case the sublist has atmost one element
        # so return it is already sorted. Just return it without doing anything
        return arr

    middle = (start + end) // 2
    # recursively called mergesort on two halves of list/sublist
    arr = mergesort(arr, start, middle)
    arr = mergesort(arr, middle + 1, end)
    return merge(arr, start, middle, end)


if __name__ == '__main__':
    arr = list(map(int, input('Enter space seperated numbers').split()))
    arr = mergesort(arr, 0, len(arr) - 1)
    print('After sorting')
    print(*arr)
