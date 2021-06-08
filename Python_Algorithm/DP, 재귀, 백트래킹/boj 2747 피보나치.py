# boj 2747 피보나치 dp 이용

dp = [True for i in range(10000)]

def fib(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    if dp[n] == True : 
        dp[n] = fib(n-1) + fib(n-2)
    return dp[n]
n = int(input())
print(fib(n))

'''
재귀 없이 루프문

n = int(input())

a, b = 0, 1

while n > 0 :
    a, b = b, a + b
    n -= 1

print(a)
