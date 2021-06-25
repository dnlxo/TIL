def binary_search(data, target) :
    low = 0
    high = len(data) - 1

    while low <= high :
        mid = (low + high)//2
        if data[mid] < target :
            low = mid + 1
        elif data[mid] > target :
            high = mid - 1
        else :
            return mid

    print('{} not in data'.format(target))

