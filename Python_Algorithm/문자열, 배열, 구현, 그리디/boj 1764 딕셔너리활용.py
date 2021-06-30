import sys
N, M = map(int, sys.stdin.readline().split())

dbj = {}
answer = []

for n in range(N) :
    name = sys.stdin.readline().rstrip()
    dbj[name] = 0

for m in range(M) :
    name = sys.stdin.readline().rstrip()
    if name in dbj :
        dbj[name] += 1

for i in dbj :
    if dbj[i] == 1 :
        answer.append(i)

print(len(answer))
for i in sorted(answer) :
    print(i)
