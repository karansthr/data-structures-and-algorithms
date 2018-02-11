def partition(arr, start, end):
    i = start
    for j in range(start, end):
        # arr[end] be the pivot
        if arr[j] <= arr[end]:
            arr[j], arr[i] = arr[i], arr[j]
            i = i + 1
    arr[end], arr[i] = arr[i], arr[end]
    return arr, i


def quick_sort(arr, start, end):
    if start >= end:
        return arr

    arr, pivot_index = partition(arr, start, end)
    arr = quick_sort(arr, start, pivot_index - 1)
    arr = quick_sort(arr, pivot_index + 1, end)
    return arr


if __name__ == '__main__':
    arr = list(map(int, input('Enter space seperated numbers:').split()))
    arr = quick_sort(arr, 0, len(arr) - 1)
    print('After sorting')
    print(*arr)
