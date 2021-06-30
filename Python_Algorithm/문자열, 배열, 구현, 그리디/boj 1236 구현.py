# boj 1236 구현
import sys
N, M = map(int, sys.stdin.readline().split())
row_cnt = [0 for n in range(N)]
column_cnt = [0 for m in range(M)]
maze2 = []
for n in range(N) :
    a = sys.stdin.readline().rstrip()
    maze2.append(a)

for n in range(N) :
    for m in range(M) :
        if maze2[n][m] == 'X' :
            row_cnt[n] = 1
            column_cnt[m] = 1

print(max(row_cnt.count(0),column_cnt.count(0)))
        

    
