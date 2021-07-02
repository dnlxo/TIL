croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

s = input().rstrip()

temp = ''
answer = 0

for i in range(len(s)) :
    temp += s[i]
    print(temp)
    if len(temp) >= 2 :
        if temp in croatia :
            answer += 1
            temp = ''
        else :
            if temp == 'dz' :
                continue
            else :
                if len(temp) == 3 :
                    temp = temp[2:]
                    answer += 2
                else :
                    temp = temp[1:]
                    answer += 1

answer += len(temp)

print(answer)
