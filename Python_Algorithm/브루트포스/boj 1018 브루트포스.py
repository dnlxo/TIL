def w_chess(mat) :
    answer = 0
    for i in range(8) :
        if i % 2 == 0 :
            for j in range(8) :
                if j % 2 == 0 :
                    if mat[i][j] == 'B' :
                        answer += 1
                else :
                    if mat[i][j] == 'W' :
                        answer += 1
        else :
            for j in range(8) :
                if j % 2 == 0 :
                    if mat[i][j] == 'W' :
                        answer += 1
                else :
                    if mat[i][j] == 'B' :
                        answer += 1
    return answer

def b_chess(mat) :
    answer = 0
    for i in range(8) :
        if i % 2 == 0 :
            for j in range(8) :
                if j % 2 == 0 :
                    if mat[i][j] == 'W' :
                        answer += 1
                else :
                    if mat[i][j] == 'B' :
                        answer += 1
        else :
            for j in range(8) :
                if j % 2 == 0 :
                    if mat[i][j] == 'B' :
                        answer += 1
                else :
                    if mat[i][j] == 'W' :
                        answer += 1
    return answer

import sys

N, M = map(int, sys.stdin.readline().split())
answer = 64
mat = []
for n in range(N) :
    mat.append(list(sys.stdin.readline().rstrip()))

for i in range(0, N-7) :
    for j in range(0, M-7) :
        temp = []
        for row in mat[i:i+8] :
            temp.append(row[j:j+8])
        answer = min(answer, w_chess(temp), b_chess(temp))

print(answer)
    
