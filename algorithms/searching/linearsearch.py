def search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return None


if __name__ == '__main__':
    arr = list(map(int, input('Enter space seperated numbers').split()))
    n = search(arr, input('Enter number to search'))
    if n:
        print("Number found !")
