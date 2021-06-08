# 재귀 구현 중요 @@@@@@

def zero(ex, i) :
    if i == n-1 :
        b = ex+str(A[i])
        c = b.replace(' ','')
        if eval(c) == 0 :
            print(b)
            return
        return
    zero(ex + str(A[i])+' ', i+1)
    zero(ex + str(A[i])+'+', i+1)
    zero(ex + str(A[i])+'-', i+1)
    

    
T = int(input())
ans = []
for t in range(T) :
    N = int(input())
    ans.append(N)
for n in ans :
    A = list(range(1,n+1))
    zero('',0)
    print()

