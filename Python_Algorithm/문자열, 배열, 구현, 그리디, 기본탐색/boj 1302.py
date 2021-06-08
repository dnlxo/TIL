# boj 1302 구현
import sys
N = int(input())
a = {}

for n in range(N) :
    name = sys.stdin.readline().rstrip()
    if name in a :
        a[name] += 1
    else :
        a[name] = 1

cnt = max(a.values())

ans = sorted(a.items(), key = lambda x : x[1], reverse = True)

q = []

for i in ans :
    if i[1] == cnt :
        q.append(i[0])
    else :
        break

print(sorted(q)[0])
