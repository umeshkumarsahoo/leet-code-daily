class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        perm=[]
        visit={n:0 for n in nums}
        for n in nums:
            visit[n]+=1
        def dfs ():
            if len(perm)==len(nums):
                res.append(perm.copy())
                return 
            for n in visit:
                if visit[n]>0:
                    perm.append(n)
                    visit[n]-=1
                    dfs()
                    visit[n]+=1
                    perm.pop()
        dfs()
        return res

        