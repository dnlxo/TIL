import sys

N, M = map(int, sys.stdin.readline().split())

lan = []
for n in range(N) :
    lan.append(int(sys.stdin.readline()))

lan.sort()

low = 1
high = max(lan)
answer = 0

while low <= high :
    mid = (low + high) // 2
    sum_lan = 0
    for i in range(len(lan)) :
        sum_lan += (lan[i] // mid)
    
    if sum_lan >= M :
        answer = mid
        low = mid + 1
    elif sum_lan < M :
        high = mid - 1
        
print(answer)
