class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ans=[]        
        ans1=[]
        a=[]
        def search(key,l):
            for i in l:
                if i[0]==key:
                    return i[1]
            return 0
        for  i in items1:
            l=search(i[0],items2)
            i[1]+=l
            if l:
                a.append(i[0])
                ans.append([i[0],i[1]])
        for i in items1:
            if i[0] not in a:
                a.append(i[0])
                ans.append(i)
        for i in items2:
            if i[0] not in a:
                a.append(i[0])
                ans.append(i)
        a=sorted(a)
        for i in range(len(a)):
            val=search(a[i],ans)
            ans1.append([a[i],val])
        print(ans1)
        return ans1 



            
        