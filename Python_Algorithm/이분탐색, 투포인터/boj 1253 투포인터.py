N = int(input())

seq = list(map(int, input().split()))

def b_search(target, alist) :
    global answer
    
    low = 0
    high = len(alist) - 1

    while high >= low :
        mid = (low + high) // 2
        
        if alist[mid] > target :
            high = mid - 1

        elif alist[mid] < target :
            low = mid + 1

        else :
            answer += 1
            return
        
ans = 0
seq.sort()

for i in range(N):
        tmp = seq[:i] + seq[i+1:]
        left, right = 0, len(tmp) - 1
        
        while left < right :
            t = tmp[left] + tmp[right]
            if t == seq[i] :
                ans += 1
                break
            
            if t < seq[i] :
                left += 1 
            else :
                right -= 1 
print(ans)
