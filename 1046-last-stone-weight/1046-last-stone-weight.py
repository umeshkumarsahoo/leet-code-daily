class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones=heapq.heapify(nums)
        while True:
            if len(stones)<=1:
                break
            stones.sort()
            y=stones.pop()
            x=stones.pop()
            if x==y:
                continue
            elif x!=y:
                stones.append(y-x)
        return stones[0] if stones else 0
            