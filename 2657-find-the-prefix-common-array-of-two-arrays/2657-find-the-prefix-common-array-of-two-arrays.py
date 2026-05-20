class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        def find(arr1,arr2):
            i,j=0,0
            res=0
            arr1.sort()
            arr2.sort()
            while i<len(arr1) and j<len(arr2):
                if arr1[i]==arr2[j]:
                    res+=1
                    i+=1
                    j+=1
                elif arr1[i]<arr2[j]:
                    i+=1
                else:
                    j+=1
            return res
        ans=[]
        for i in range(len(A)):
            ans.append(find(A[:i+1],B[:i+1]))
        return ans


        