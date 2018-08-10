def max_subarray(arr):
    '''
    return max sum of contigous subarray

    :param arr: input list of numbers
    :type arr: list
    :return : maximux sum of contigous subarray
    :rtype: int
    '''
    max_sum = current_maximum = arr[0]
    for element in arr[1:]:
        current_maximum = max(element, element+current_maximum)
        max_sum = max(max_sum, current_maximum)
    return max_sum


if __name__ == '__main__':
    for test in range(int(input())):
        _ = input()
        arr = list(map(int, input().split()))
        print(max_subarray(arr))
