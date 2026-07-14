class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        sorted_elements = sorted(d.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_elements[:k]]