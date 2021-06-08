import sys
N = int(sys.stdin.readline())
budget = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

budget.sort()

low = 0
high = budget[-1]
answer = 0

while low <= high :
    mid = (low + high) // 2
    b_sum = 0
    for i in budget :
        if i < mid : 
            b_sum += i
        else :
            b_sum += mid
            
    if b_sum > M :
        high = mid - 1
    else :
        answer = mid
        low = mid + 1

print(answer)
