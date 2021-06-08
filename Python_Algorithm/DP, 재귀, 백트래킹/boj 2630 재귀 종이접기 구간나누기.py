import sys

N = int(sys.stdin.readline())

paper = []

for n in range(N) :
    paper.append(list(map(int, sys.stdin.readline().split())))

answer = [0,0] # white, blue

def w_check(mat) :
    for i in range(len(mat)) :
        for j in range(len(mat)) :
            if mat[i][j] == 1 :
                return False
    else :
        return True

def b_check(mat) :
    for i in range(len(mat)) :
        for j in range(len(mat)) :
            if mat[i][j] == 0 :
                return False
    else :
        return True
    
def cut(paper) :
    global answer
    M = len(paper)
    if b_check(paper) :
        answer[1] += 1
        return
    if w_check(paper) :
        answer[0] += 1
        return
    
    paper1 = []
    for i in range(M//2) :
        paper1.append(paper[i][:M//2])
    paper2 = []
    for i in range(M//2) :
        paper2.append(paper[i][M//2:])
    paper3 = []
    for i in range(M//2, M) :
        paper3.append(paper[i][:M//2])
    paper4 = []
    for i in range(M//2, M) :
        paper4.append(paper[i][M//2:])
    cut(paper1)
    cut(paper2)
    cut(paper3)
    cut(paper4)

cut(paper)
for i in answer :
    print(i)
    
