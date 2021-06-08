n = int(input())
m = n
def cycle(a) :
    b = str(a)
    if a < 10 :
        return a*10 + a
    else :
        return int(str(b[-1]) + str(int(b[0]) + int(b[1]))[-1])

answer = 0

if n == 0 :
    print(1)
else :
    while True :
        answer += 1
        n = cycle(n)
        if n == m :
            print(answer)
            break
