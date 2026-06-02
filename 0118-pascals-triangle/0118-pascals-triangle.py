class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        prev=[]
        for i in range(1,numRows+1):
            if not prev  and i==1: 
                prev=[1]*i
            elif i==2:
                prev=[1]*i
            else:
                ans=[1]*i
                for i in range(1,len(prev)):
                    ans[i]=prev[i-1]+prev[i]
                prev=ans
            res.append(prev)
        return res




