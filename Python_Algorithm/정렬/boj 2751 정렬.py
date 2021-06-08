import sys
N = int(sys.stdin.readline())
a = []
for n in range(N) :
    a.append(int(sys.stdin.readline()))

for i in sorted(a) :
    print(i)
