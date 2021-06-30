N = int(input())

dic = []
answer = 0
for n in range(N) :
    string = input()
    if string in dic :
        continue
    else :
        answer += 1
        for i in range(len(string)) :
            dic.append(string[i:] + string[:i])
print(answer)
