class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        mini,maxi=min(need1,need2),max(need1,need2)
        no_overlap=cost1*need1+cost2*need2
        overlap=costBoth*mini+(need1-mini)*cost1+(need2-mini)*cost2
        whole=maxi*costBoth
        return min(no_overlap,overlap,whole)
        
        