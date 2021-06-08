# boj 11004
import sys
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

print(sorted(A)[K-1])
