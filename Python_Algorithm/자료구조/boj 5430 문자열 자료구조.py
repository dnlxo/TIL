import sys
from collections import deque

T = int(input())

for t in range(T) :
    command = sys.stdin.readline().rstrip()
    N = int(input())
    
    a = sys.stdin.readline().rstrip()[1:-1]
    if a == '' :
        seq = deque([])
    else :
        seq = deque(list(map(int, a.split(','))))

    #앞 True
    flag = True
    breaking = False
    
    for c in command :
        if c == 'R' :
            flag = not flag
            
        elif c == 'D' :
            if flag :
                if seq :
                    seq.popleft()
                else :
                    print('error')
                    breaking = True
                    break
            else :
                if seq :
                    seq.pop()
                else :
                    print('error')
                    breaking = True
                    break

    if breaking :
        continue
    
    if flag :
        print('[', end='')
        while seq :
            if len(seq) == 1 :
                print(seq.popleft(), end = '')
            else :
                print(seq.popleft(), end = ',')
        print(']')
    else :
        print('[', end='')
        while seq :
            if len(seq) == 1 :
                print(seq.pop(), end = '')
            else :
                print(seq.pop(), end = ',')
        print(']')
            
