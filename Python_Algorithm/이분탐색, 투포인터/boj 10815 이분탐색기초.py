import sys
N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

check = list(map(int, sys.stdin.readline().split()))

def bin_search(alist, target) :
    low = 0
    high = len(alist) - 1
    while low <= high :
        mid = (low + high) // 2
        if alist[mid] == target :
            return 1
        elif alist[mid] > target :
            high = mid - 1
        else :
            low = mid + 1
    return 0

num_list.sort()

for i in check :
    print(bin_search(num_list, i), end = ' ')
