# boj 1668 구현

N = int(input())
trp = []
for n in range(N) :
    trp.append(int(input()))

def cnt(alist) :
    count = 1
    max_trp = alist[0]
    for i in range(len(alist) - 1) :
        if max_trp < alist[i+1] :
            count += 1
            max_trp = alist[i+1]
    return count

print(cnt(trp))
print(cnt(list(reversed(trp))))
