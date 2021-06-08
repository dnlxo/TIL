n = int(input())

name = []

for _ in range(n) :
    name.append(input())
length = len(name[0])
answer = name[0]

for i in range(1, n) :
    compare = ''
    for j in range(length) :
        if name[i][j] == answer[j] :
            compare += answer[j]
        else :
            compare += '?'
    answer = compare

print(answer)
