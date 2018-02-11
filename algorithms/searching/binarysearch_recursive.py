def search(arr, key, start=None, end=None):
    if start is end is None:
        start, end = 0, len(arr)-1
    if start >= end:
        return -1
    middle = (start + end) // 2
    if key == arr[middle]:
        return middle
    elif key > arr[middle]:
        return search(arr, key, middle + 1, end)
    else:
        return search(arr, key, start, middle - 1)


if __name__ == '__main__':
    arr = list(map(int, input('Enter space seperated numbers : ').split()))
    n = search(arr, int(input('Enter number to search : ')))
    if n >= 0:
        print("Key found at index", n)
    else:
        print("Key not found")
