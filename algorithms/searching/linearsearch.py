def search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == '__main__':
    arr = list(map(int, input('Enter space seperated numbers : ').split()))
    n = search(arr, int(input('Enter number to search : ')))
    if n >= 0:
        print("Number found at index", n)
    else:
        print("Number not found !")
