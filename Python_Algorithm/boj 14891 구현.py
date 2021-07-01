import sys

def rotate(s,v) :
    if v == 1 :
        return s[-1]+s[:-1]
    elif v == -1 :
        return s[1:]+s[0]

gears = ['']

for g in range(4) :
    gears.append(sys.stdin.readline().rstrip())

K = int(input())

for k in range(K) :
    gear, v = map(int, sys.stdin.readline().split())

    gorotate = [False]*5
    
    connect = [False]*3
    
    if gears[1][2] != gears[2][-2] :
        connect[0] = True    
    if gears[2][2] != gears[3][-2] :
        connect[1] = True
    if gears[3][2] != gears[4][-2] :
        connect[2] = True
        
    if gear == 1 :
        if connect[0] :
            gorotate[2] = True
            if connect[1] :
                gorotate[3] = True
                if connect[2] :
                    gorotate[4] = True
                    
    elif gear == 2 :
        if connect[1] :
            gorotate[3] = True
            if connect[2] :
                gorotate[4] = True
        if connect[0] :
            gorotate[1] = True
            
    elif gear == 3 :
        if connect[1] :
            gorotate[2] = True
            if connect[0] :
                gorotate[1] = True
        if connect[2] :
            gorotate[4] = True
            
    else :
        if connect[2] :
            gorotate[3] = True
            if connect[1] :
                gorotate[2] = True
                if connect[0] :
                    gorotate[1] = True

    temp = rotate(gears[gear], v)
    gears[gear] = temp

    for i in range(1,5) :
        if gorotate[i] :
            if gear % 2 == 1 :
                if i % 2 == 1 :
                    temp = rotate(gears[i], v)
                    gears[i] = temp
                else :
                    temp = rotate(gears[i], -v)
                    gears[i] = temp
            if gear % 2 == 0 :
                if i % 2 == 0 :
                    temp = rotate(gears[i], v)
                    gears[i] = temp
                else :
                    temp = rotate(gears[i], -v)
                    gears[i] = temp
                    

answer = 0
cnt = 1
for i in range(1,5) :
    answer += cnt*(int(gears[i][0]))
    cnt *= 2

print(answer)
    
