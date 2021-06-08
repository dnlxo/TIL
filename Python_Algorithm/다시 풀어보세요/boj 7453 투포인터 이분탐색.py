import sys
n = int(sys.stdin.readline())
A = []
B = []
C = []
D = []
for i in range(n) :
    a,b,c,d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
dic = {}
answer = 0

for i in A :
    for j in B :
        if i+j in dic :
            dic[i+j] += 1
        else :
            dic[i+j] = 1

for i in C :
    for j in D :
        if -(i+j) in dic :
            answer += dic[-i-j]

print(answer)

#아래는 이분탐색 코드 시간초과 남 병신 이걸로 풀으라매
import sys
n = int(sys.stdin.readline())
A = []
B = []
C = []
D = []
for i in range(n) :
    a,b,c,d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
AB = []
CD = []
for i in A :
    for j in B :
        AB.append(i+j)
for i in C :
    for j in D :
        CD.append(i+j)

CD.sort()

def upper_bound(data, target) :
    low = 0
    high = len(data)
    while low < high :
        mid = (low + high) // 2
        if target >= data[mid] :
            low = mid + 1
        else :
            high = mid
    return low

def lower_bound(data, target) :
    low = 0
    high = len(data)
    while low < high :
        mid = (low + high) // 2
        if target <= data[mid] :
            high = mid
        else :
            low = mid + 1
    return low

def bin_search(alist, i) :
    return upper_bound(alist, i) - lower_bound(alist, i)
    
answer = 0

for i in AB :
    answer += bin_search(CD, -i)

print(answer)
