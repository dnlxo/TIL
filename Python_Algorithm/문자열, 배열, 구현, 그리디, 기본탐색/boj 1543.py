# boj 1543 그리디, 기본탐색

import sys
words = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()
cnt = 0
m_words = words.replace(word,'0')
for i in m_words :
    if i == '0' :
        cnt += 1
print(cnt)
