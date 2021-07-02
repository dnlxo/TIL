A, B, C = map(int, input().split())

def my_mod(A, B) :
    if B == 1 :
        return A % C
    save = my_mod(A, B//2)
    if B % 2 == 0 : # 짝수의 경우
        return save * save % C
    else :
        return save * save * (A % C) % C

print(my_mod(A, B))
