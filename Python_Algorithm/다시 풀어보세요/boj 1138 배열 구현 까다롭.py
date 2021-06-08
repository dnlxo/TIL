N = int(input())
people = list(map(int, input().split()))

answer = [0]*N # 정답배열 만들어두기 

for i in range(1, N+1) : # 키 1인 사람부터 순서대로 돕니다. 
    a = people[i-1] # 키 1인 사람 보다 왼쪽에 있으면서 키 큰사람 수
    cnt = 0 
    for j in range(N) : # 차례대로 한 사람씩 자리 찾기
        if cnt == a and answer[j] == 0 :
            answer[j] = i
            break
        elif answer[j] == 0 :
            cnt += 1

print(*answer)
