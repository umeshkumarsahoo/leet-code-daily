class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort() 

        def back_track(arr, index, total):
            if total == target:
                result.append(arr[:]) 
                return
            if total > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                arr.append(candidates[i])
                back_track(arr, i + 1, total + candidates[i])
                arr.pop()

        back_track([], 0, 0)
        return result
            

            
        
        