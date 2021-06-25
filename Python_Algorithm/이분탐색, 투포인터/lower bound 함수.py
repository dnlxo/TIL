def lower_bound(data, target) :
    low = 0
    high = len(data)
    while low < high :
        mid = (low + high) // 2
        if target <= data[mid] :
            high = mid
        else :
            low = mid + 1
    return low
