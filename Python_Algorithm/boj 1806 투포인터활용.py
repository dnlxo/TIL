import sys

N, S = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split())) + [0]

a, b = 0, 0
cur_sum = nums[0]

answer = []

while b < N :

    if cur_sum >= S :
        answer.append(b+1 - a)
        cur_sum -= nums[a]
        a += 1

    else :
        b += 1
        cur_sum += nums[b]

    
if answer == [] :
    print(0)
else :
    print(min(answer))
