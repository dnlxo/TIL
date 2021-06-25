import sys
N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

check = list(map(int, sys.stdin.readline().split()))

def lower_bound(alist, target) :
    low = 0
    high = len(alist)
    while low < high :
        mid = (low + high) // 2
        if alist[mid] >= target :
            high = mid
        else :
            low = mid + 1
    return mid

def upper_bound(alist, target) :
    low = 0
    high = len(alist)
    while low < high :
        mid = (low + high) // 2
        if alist[mid] <= target :
            low = mid + 1
        else :
            high = mid
    return mid


num_list.sort()

for i in check :
    print((upper_bound(num_list, i) - lower_bound(num_list, i)), end = ' ')
