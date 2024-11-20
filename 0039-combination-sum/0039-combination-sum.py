class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def make_comb(arr,i,total):
            if total==target:
                result.append(arr[:])
                return 
            if total>target or i>=len(candidates):
                return 
            arr.append(candidates[i])
            make_comb(arr,i,total+candidates[i])
            arr.pop()
            make_comb(arr,i+1,total)
            return result
        return make_comb([],0,0)
        