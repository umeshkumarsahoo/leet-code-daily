class Solution:
    def checkBoquet(self,day,m,k,bloomDay)->bool:
        arr=[0]*len(bloomDay)
        b=0
        n=0
        for i in range(len(bloomDay)):
            if bloomDay[i]<=day:
                arr[i]='X'
        for i in range(len(arr)):
            if arr[i]=='X':
                n+=1
                if n==k:
                    n=0
                    b+=1
            else:
                n=0

        return True if b>=m else False
        
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        ans=0
        if m*k>len(bloomDay):
            return -1
            
        start=min(bloomDay)
        end=max(bloomDay)
        while start<=end:
            mid=(start+end)//2
            if self.checkBoquet(mid,m,k,bloomDay):
                ans=mid
                end=mid-1
            else :
                start=mid+1
        return ans
        