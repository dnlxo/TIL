import sys

N = int(sys.stdin.readline())
dic = {}
alpha = []
for i in range(26) :
    alpha.append(chr(65+i))
cnt = 9
answer = 0
for n in range(N) :
    word = sys.stdin.readline().rstrip()
    for alp in alpha :
        temp = ''
        for i in range(len(word)) :
            if word[i] == alp :
                temp += '1'
            else :
                temp += '0'
        if alp in dic :
            dic[alp] += int(temp)
        else : 
            dic[alp] = int(temp)
            
for i in sorted(dic.items(), key = lambda x : x[1], reverse = True) :
    answer += i[1]*cnt
    cnt -= 1

print(answer)
