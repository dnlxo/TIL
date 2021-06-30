A, B = input().split()

A = '0b' + A
B = '0b' + B

answer = format(int(A, 2) + int(B, 2), 'b')
print(answer)
