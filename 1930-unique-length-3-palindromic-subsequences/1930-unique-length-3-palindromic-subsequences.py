class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        count = 0
        for char in letters:
            left = -1
            right = -1
            for i, c in enumerate(s):
                if c == char:
                    if left == -1:
                        left = i
                    right = i
            if left != right:
                count += len(set(s[left + 1:right]))
        return count