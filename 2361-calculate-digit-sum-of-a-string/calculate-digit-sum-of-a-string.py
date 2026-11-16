class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            res = []
            for i in range(0, len(s), k):
                group = s[i:i+k]
                group_sum = sum(int(ch) for ch in group)
                res.append(str(group_sum))
            s = "".join(res)
        return s