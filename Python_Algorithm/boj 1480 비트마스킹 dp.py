import sys
N, M, C = map(int, sys.stdin.readline().split())
gem_list = list(map(int, sys.stdin.readline().split()))

dp = [[[0 for i in range(C+1)] for j in range(M+1)] for k in range(1 << 14)]


def solution(gems, bag_idx, current_capacity) :
    # 가방 다 썼거나, 보석 다 썼으면 ?
    if gems == ((1 << N) - 1) or bag_idx >= M :
        return 0
        

    if dp[gems][bag_idx][current_capacity] != 0 :
        return dp[gems][bag_idx][current_capacity]

    now_answer = 0

    for i in range(N) : # 모든 보석을 돌면서 하나씩 다 넣어본다.
        
        if (gems & (1 << i)) != 0 or gem_list[i] > C : # 지금 쓸려는 보석이 이미 사용한 보석이면..?
            continue
        
        if (current_capacity >= gem_list[i]) :# 지금 가방에 넣을 수 있으면 ?
            now_answer = max(now_answer, solution(gems | (1 << i), bag_idx, current_capacity - gem_list[i]) + 1)

        else :
            now_answer = max(now_answer, solution(gems, bag_idx + 1, C))


    dp[gems][bag_idx][current_capacity] = now_answer
    return now_answer

print(solution(0, 0, C))
        

    
