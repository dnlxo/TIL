import sys

N = int(sys.stdin.readline())
times = []
for n in range(N) :
    times.append(list(map(int, sys.stdin.readline().split())))

# 일찍 끝나는 순서로 정렬

times.sort()
# 같은 end time 내에서
# 빠른 start time 순으로 정렬 되어있어야 한다.
# [[4, 4], [3, 4], [2, 4]] 의 경우 [4, 4] 만하고 끝나버리기 때문
times.sort(key = lambda x : x[1])

answer = 0
end = 0

for t in times :
    if t[0] >= end : # 회의 시간 겹치지 않기 위해..
        answer += 1
        end = t[1]

print(answer)
