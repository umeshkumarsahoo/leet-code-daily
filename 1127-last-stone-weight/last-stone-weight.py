import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        max_stone=[-stone for stone in stones]
        heapq.heapify(max_stone)
        while len(max_stone)>1:
            a=heapq.heappop(max_stone)
            b=heapq.heappop(max_stone)
            rem=a-b
            if rem==0:
                continue
            else:
                heapq.heappush(max_stone,rem)
        return -max_stone[0] if max_stone else 0

