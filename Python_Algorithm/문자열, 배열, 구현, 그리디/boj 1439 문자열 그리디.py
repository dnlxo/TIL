import sys
s = sys.stdin.readline().rstrip()


s = 's' + s
cnt0 = 0
cnt1 = 0
for i in range(1, len(s)) :
    if s[i] == '0' and s[i-1] != '0' :
        cnt0 += 1
    if s[i] == '1' and s[i-1] != '1' :
        cnt1 += 1

print(min(cnt0, cnt1))
