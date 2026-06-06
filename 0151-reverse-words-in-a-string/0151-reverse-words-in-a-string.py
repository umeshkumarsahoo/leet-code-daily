class Solution:
    def reverseWords(self, s: str) -> str:
        arr=s.strip().split()
        return " ".join(arr[::-1])
        