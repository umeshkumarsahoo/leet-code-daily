class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming=collections.defaultdict(list)
        for src,dest in edges:
            incoming[dest].append(src)
        res=[]
        for  i in range(n):
            if not incoming[i]:
                res.append(i)
        return res
        