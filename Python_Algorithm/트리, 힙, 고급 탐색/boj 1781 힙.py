import sys
import heapq
N = int(sys.stdin.readline())
quiz = []
for n in range(N) :
    dead, cup = map(int, sys.stdin.readline().split())
    quiz.append((dead, cup))

cnt = 0
answer = 0
heap = []

quiz.sort(reverse = True)
time = quiz[0][0]

while time >= 1 :
    while cnt < N and quiz[cnt][0] == time :
        heapq.heappush(heap, -quiz[cnt][1])
        cnt += 1

    if heap :
        answer -= heapq.heappop(heap)

    time -= 1
    
print(answer)
