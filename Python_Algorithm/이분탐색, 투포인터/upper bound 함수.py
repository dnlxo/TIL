def upper_bound(data, target) :
    low = 0
    high = len(data)
    while low < high :
        mid = (low + high) // 2
        if target >= data[mid] :
            low = mid + 1
        else :
            high = mid
    return low
