class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = 0
        for i in range(len(word)):
            if word[i] == ch:
                idx = i
                break
        if idx == 0:
            return word
        part_a = word[:i+1]
        part_b = word[i+1:]
        return part_a[::-1] + part_b
