import sys

N, M = map(int, sys.stdin.readline().split())
q = [0]*(N+1)
connect = [[] for n in range(N+1)]
for m in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    q[b] += 1
    connect[a].append(b)
answer = []
while len(answer) < N :
    for idx in range(1, N+1) :
        if q[idx] == 0 :
            answer.append(idx)
            q[idx] = None
            for i in connect[idx] :
                q[i] -= 1
            break
    
print(*answer)
