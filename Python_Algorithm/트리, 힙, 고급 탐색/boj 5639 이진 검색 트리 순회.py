# boj 5639 이진 검색 트리

values = []
import sys
sys.setrecursionlimit(20000)

def post(alist) :
    M_idx = len(alist)
    m_idx = 1
    if len(alist) == 1 :
        print(alist[0])
        return
    elif len(alist) == 0 :
        return
    for i in range(1, len(alist)) :
        if alist[i] < alist[0] :
            m_idx = i
            break
    for i in range(1, len(alist)) :
        if alist[i] > alist[0] :
            M_idx = i
            break
    post(alist[m_idx:M_idx])
    post(alist[M_idx:])
    print(alist[0])

while True:
    try:
        values.append(int(sys.stdin.readline()))
        
    except:
        break

post(values)
