# boj 2003 수들의 합 투포인터
# i got two pointer a and b
# 투포인터는 매번 구간합을 구하면 안된다. 느림!
# 갱신만 해야됨

import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.append(0)
def tp(seq, M) : #수열과 목표 합 받는 함수
    cnt = 0
    a, b = 0, 0
    seq_sum = seq[a]
    while b < N : #b 포인터가 끝까지 가면 루프 끝
        if seq_sum == M :
            cnt += 1
            b += 1
            seq_sum = seq_sum - seq[a] + seq[b]
            a += 1
        elif seq_sum > M :
            seq_sum -= seq[a]
            a += 1
        else :
            b += 1
            seq_sum += seq[b]
    return cnt

print(tp(A, M))
        
