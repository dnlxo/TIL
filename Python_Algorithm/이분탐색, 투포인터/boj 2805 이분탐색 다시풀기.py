import sys

N, M = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))

tree.sort()

low = 0
high = max(tree)
answer = 0

while low <= high :
    mid = (low + high) // 2
    for i in range(len(tree)) :
        if tree[i] >= mid :
            cut_line = i
            break
    sum_tree = sum(tree[cut_line:]) - mid*len(tree[cut_line:])
    if sum_tree >= M :
        answer = mid
        low = mid + 1
    elif sum_tree < M :
        high = mid - 1
        
print(answer)
