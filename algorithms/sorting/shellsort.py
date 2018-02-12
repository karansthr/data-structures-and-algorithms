def shell_sort(arr):
    pass


if __name__ == '__main__':
    arr = list(map(int, input('Enter space seperated numbers:').split()))
    arr = shell_sort(arr)
    print('After sorting')
    print(*arr)
