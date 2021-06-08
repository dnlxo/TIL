import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
product = list(map(int, sys.stdin.readline().split()))
prod = set(product)
plug = set()
answer = 0

for i in range(K) :
    if product[i] in plug :
        continue
    else :
        if len(plug) < N :
            plug.add(product[i])
        else :
            temp = []
            for k in plug :
                if k not in product[i:] :
                    j = k
                    break
                else : 
                    temp.append((product[i:].index(k), k))
            else :
                temp.sort()
                j = temp[-1][1]
            plug.remove(j)
            plug.add(product[i])
            answer += 1

print(answer)
