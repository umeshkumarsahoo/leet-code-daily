import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        def remove(n):
            return n//2
        maxPiles=[-pile for pile in piles]
        heapq.heapify(maxPiles)
        for _ in range(k):
            large= -heapq.heappop(maxPiles)
            remain=large-remove(large)
            heapq.heappush(maxPiles,-remain)
        return -sum(maxPiles)


        