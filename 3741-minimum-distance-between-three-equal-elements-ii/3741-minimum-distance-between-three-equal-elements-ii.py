
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = defaultdict(list)
        for i, num in enumerate(nums):
            positions[num].append(i)

        min_dist = float('inf')

        for pos_list in positions.values():
            if len(pos_list) < 3:
                continue
            for i in range(len(pos_list) - 2):
                a = pos_list[i]
                c = pos_list[i+2]

                dist = 2 * (c - a)
                min_dist = min(min_dist, dist)

        return min_dist if min_dist != float('inf') else -1