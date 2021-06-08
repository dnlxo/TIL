# boj 2805 binary search

import sys

N, M = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))

def bs(data, target) :
    low = 0
    high = max(tree)
    
    while low <= high :
        mid = (low + high)//2
        cnt = 0
        
        for i in tree :
            if i > mid :
                cnt += i - mid
                
        if cnt < target :
            high = mid - 1
            
        elif cnt > target :
            low = mid + 1
            ans = mid #가지고 가려는 나무 길이보다 많이 자를 수 밖에 없는 경우
        else :
            return mid
    return ans

print(bs(tree, M))
