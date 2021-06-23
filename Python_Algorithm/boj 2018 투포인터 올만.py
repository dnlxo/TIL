N = int(input())

a, b = 0, 0
cur_sum = 1

answer = 0

while b < N :

    if cur_sum == N :
        answer += 1
        cur_sum -= a + 1
        a += 1
        b += 1
        cur_sum += b + 1 

    elif cur_sum > N :
        cur_sum -= a + 1
        a += 1

    else :
        b += 1
        cur_sum += b + 1

    
print(answer)
