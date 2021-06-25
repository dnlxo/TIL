X,Y = map(int, input().split())

Z = int((Y*100/X))

low = 1
high = 1000000000
answer = 0

while low <= high :
    if Z == 99 or Z == 100 :
        answer = -1
        break
    mid = (low + high) // 2
    if Z == int(((Y+mid)*100/(X+mid))) :
        low = mid + 1
    else :
        high = mid - 1
        answer = mid

print(answer)
