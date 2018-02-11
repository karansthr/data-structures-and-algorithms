def search(arr, key):
    start, end = 0, len(arr) - 1
    while (True):
        middle = (start + end) // 2
        if key == arr[middle]:
            return middle
        elif key > arr[middle]:
            start = middle + 1
        else:
            end = middle - 1

        if start >= end:
            return -1  # -1 should be interpreted as not found by calling
            # function


if __name__ == '__main__':
    arr = list(map(int, input('Enter space seperated numbers').split()))
    n = search(arr, int(input('Enter number to search')))
    if n >= 0:
        print("Key found at index", n)
    else:
        print("Key not found")
