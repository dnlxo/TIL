import sys
from collections import deque

N = int(sys.stdin.readline())
crane = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

box = deque(box)
temp = deque([])

cnt = 0
answer = 0

if max(box) > max(crane) :
    print(-1)
else :
    while box :

        for i in crane :
            j = 0
            while True :
                if not box :
                    break
                if box[j] <= i :
                    box.popleft()
                    break
                else :
                    temp.append(box.popleft())
        

        box = temp + box
        temp = deque([])
        cnt += 1

    print(cnt)
