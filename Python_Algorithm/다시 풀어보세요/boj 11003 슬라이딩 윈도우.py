import sys
from collections import deque
N, L = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

window = deque([]) # 숫자와 idx 같이 저장
cnt = 0
answer = []
minimum = 0

for i in range(N) :
    print(nums[i])
    print(window)
    while window and window[-1][0] > nums[i] :
    # 새로운거 들어오기 전에 뺄거 확인
        window.pop()

    if window and i - window[0][1] >= L :
    # window 크기 벗어나면 앞에꺼 빼기
        window.popleft()
        
    window.append((nums[i], i))
    answer.append(window[0][0])
    print(window)
print(*answer)

