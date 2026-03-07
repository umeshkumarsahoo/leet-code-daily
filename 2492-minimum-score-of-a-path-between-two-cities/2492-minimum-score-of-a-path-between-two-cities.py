class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj=defaultdict(list)
        for src,dst,cost in roads:
            adj[src].append([dst,cost])
            adj[dst].append([src,cost])
        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            nonlocal res
            for nei,cost in adj[i]:
                res=min(res,cost)
                dfs(nei)
            
        res=float('inf')
        visit=set()
        dfs(1)
        return res
        