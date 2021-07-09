def topology(build_time, preceding, next_build) :


T = int(input())

for t in range(T) :
    N, K = map(int, input().split())

    build_time = list(map(int, input().split()))
    next_build = [[] for n in range(N+1)]
    preceding = [0 for n in range(N+1)]

    for k in range(K) :
        i, j = map(int, input().split())
        next_build[i].append(j)
        preceding[j] += 1
        
    W = int(input())

    
