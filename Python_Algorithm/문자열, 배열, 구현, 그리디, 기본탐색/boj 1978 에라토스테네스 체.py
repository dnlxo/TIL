import sys

N = int(input())

prime = list(map(int, sys.stdin.readline().split()))
m = max(prime) + 1
sieve = [True] * m
sieve[0] = False
sieve[1] = False

for i in range(2, int(m ** 0.5) + 1) :
    if sieve[i] == True :
        for j in range(i*2, m, i) :
            sieve[j] = False

answer = 0

for i in prime :
    if sieve[i] == True :
        answer += 1

print(answer)
