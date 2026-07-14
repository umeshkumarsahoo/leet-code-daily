from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = Counter(x for x in nums if x % 2 == 0)
        if not counts:
            return -1
        
        max_freq = -1
        ans = -1
        for num, freq in counts.items():
            if freq > max_freq:
                max_freq = freq
                ans = num
            elif freq == max_freq:
                ans = min(ans, num)
                
        return ans