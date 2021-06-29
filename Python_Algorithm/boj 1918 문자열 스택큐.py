from collections import deque

string = input().rstrip()

temp = deque()
answer = []
flag = 0

for i in range(len(string)) :
    if string[i] == '+' or string[i] == '-' or string[i] == '/' or string[i] == '*' :
        
        if string[i] == '+' or string[i] == '-' :
            if flag == 0 or string[i-2] != '(' :
                if temp :
                    if temp[0] == '+' or temp[0] == '-' :
                        answer.append(temp.popleft())
                    elif temp[0] == '*' or temp[0] == '/' :
                        answer.append(temp.popleft())
                        if 
                        
        else :
            if flag == 0 :
                if temp :
                    if temp[0] == '*' or temp[0] == '/' :
                        answer.append(temp.popleft())
                         
        temp.appendleft(string[i])
        
    elif string[i] == '(' :
        flag += 1

    elif string[i] == ')' :
        flag -= 1
        if temp :
            answer.append(temp.popleft())
        
    else :
        answer.append(string[i])

while temp :
    answer.append(temp.popleft())

print(''.join(answer))
