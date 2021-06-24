import sys
N = int(input())
dic = {}
for n in range(N) :
    name, log = sys.stdin.readline().split()
    if log == 'enter' :
        dic[name] = 1
    else :
        dic[name] = 0

member = []

for i in dic :
    if dic[i] == 1 :
        member.append(i)

member.sort(reverse = True)

for m in member :
    print(m)
