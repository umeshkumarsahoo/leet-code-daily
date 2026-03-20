class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        res = 0
        j = 0
        best = 0
        
        for work in worker:
            while j < len(jobs) and work >= jobs[j][0]:
                best = max(best, jobs[j][1])
                j += 1
            res += best
        
        return res