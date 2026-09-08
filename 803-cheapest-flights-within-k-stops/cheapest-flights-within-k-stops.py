class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 1. Build adjacency list: node -> list of (neighbor, price)
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))
            
        # 2. Queue stores (current_node, current_cost)
        q = [(src, 0)]
        
        # 3. Track minimum cost to reach each node
        minCost = [float('inf')] * n
        minCost[src] = 0
        
        stops = 0
        
        # 4. Level-by-level BFS up to k stops (k stops = k + 1 edges)
        while q and stops <= k:
            size = len(q)
            for _ in range(size):
                currNode, cost = q.pop(0)
                
                for neighbor, price in adj[currNode]:
                    newCost = cost + price
                    
                    # Only explore if we found a cheaper way to reach this neighbor
                    if newCost < minCost[neighbor]:
                        minCost[neighbor] = newCost
                        q.append((neighbor, newCost))
                        
            stops += 1
            
        return -1 if minCost[dst] == float('inf') else minCost[dst]