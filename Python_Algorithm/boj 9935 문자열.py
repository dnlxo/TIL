from collections import deque
import sys

string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

que = []
for i in string :
    que.append(i)
    if i == bomb[-1] and len(que) >= len(bomb) :
        if ''.join(que[-len(bomb):]) == bomb :
            for n in range(len(bomb)) :
                que.pop()

string = ''.join(que)

if string == '' :
    print('FRULA')
else :
    print(string)    
