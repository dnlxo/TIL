import sys
from collections import deque
N = int(input())
M = int(input())
vote = list(map(int, sys.stdin.readline().split()))

dic = {}
temp = []
photo = [0]*N + [-1]

for i in range(M) :
    for j in range(N) :
        
        if photo[j] == 0 :
            photo[j] = vote[i]
            dic[vote[i]] = 1
            break
        elif photo[j] == vote[i] :
            dic[vote[i]] += 1
            break
        else :
            if 0 in photo :
                continue
            elif vote[i] in photo :
                dic[vote[i]] += 1
                break
            else :
                if photo[j] == sorted(dic.items(), key = lambda x : x[1])[0][0] :
                    dic.pop(photo[j])
                    photo[j] = vote[i]
                    dic[vote[i]] = 1
                    
                    break

print(*sorted(photo)[1:])
        
                
                
        
    
