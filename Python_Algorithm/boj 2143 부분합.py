import sys
T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

dic = {}
answer = 0

for i in range(n) :
    for j in range(i+1, n+1) :
        subsum = sum(A[i:j])
        if T - subsum in dic :
            dic[T - subsum] += 1
        else :
            dic[T - subsum] = 1

for i in range(m) :
    for j in range(i+1, m+1) :
        subsum = sum(B[i:j])
        if subsum in dic :
            answer += dic[subsum]
        

print(answer)
