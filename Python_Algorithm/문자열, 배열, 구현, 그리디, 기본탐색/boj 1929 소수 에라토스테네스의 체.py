a, b = map(int, input().split())

prime = [True]*(b+1)

prime[0] = False
prime[1] = False

primes = []

for i in range(2, b+1) :
    if prime[i] :
        primes.append(i)
        for j in range(i*2, b+1, i) :
            prime[j] = False

for i in primes :
    if a <= i <= b :
        print(i)
