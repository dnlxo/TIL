import sys
s1 = '0' + sys.stdin.readline().rstrip()
s2 = '0' + sys.stdin.readline().rstrip()

dp = [[0 for i in range(len(s1))] for j in range(len(s2))]

for i in range(1, len(s2)) :
    for j in range(1, len(s1)) :
        if s2[i] == s1[j] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
def print_lcs(i, j) :
    if dp[i][j] == 0 :
        return ''
    while dp[i][j] == dp[i][j-1] :
        j -= 1
    return print_lcs(i-1,j-1) + s1[j]
print(print_lcs(len(s2)-1, len(s1)-1))

