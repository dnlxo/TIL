import heapq
import sys

T = int(input())

for t in range(T) :
    K = int(input())
    answer = []
    mheap = []
    Mheap = []
    deleted = {}
    for k in range(K) :
        cmd = sys.stdin.readline().rstrip()
        if cmd == 'D 1' :
            if Mheap :
                if deleted[-Mheap[0]] >= 1 :
                    deleted[-heapq.heappop(Mheap)] -= 1
                else :
                    while True :
                        -heapq.heappop(Mheap)
                        if not Mheap :
                            break
                        if deleted[-Mheap[0]] >= 1 :
                            deleted[-heapq.heappop(Mheap)] -= 1
                            break
                
        elif cmd == 'D -1' :
            if mheap :
                if deleted[mheap[0]] >= 1 :
                    deleted[heapq.heappop(mheap)] -= 1
                else :
                    while True :
                        heapq.heappop(mheap)
                        if not mheap :
                            break
                        if deleted[mheap[0]] >= 1 :
                            deleted[heapq.heappop(mheap)] -= 1
                            break

        else :
            num = int(cmd[2:])
            if num in deleted :
                deleted[num] += 1
            else :
                deleted[num] = 1
            heapq.heappush(mheap, num)
            heapq.heappush(Mheap, -num)
        print(deleted)
    for i in deleted :
        if deleted[i] >= 1 :
            answer.append(i)
            
    if answer == [] :
        print('EMPTY')
    else :
        print(max(answer), min(answer))
    print(answer)
