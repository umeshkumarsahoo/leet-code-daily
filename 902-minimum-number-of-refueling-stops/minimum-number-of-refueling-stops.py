class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        miss=[]
        time=0
        prev=0
        f=startFuel
        stations.append([target,0])
        for pos,gas in stations:
            dist,prev=pos-prev,pos
            if f<dist:
                while miss and f<dist:
                    time+=1
                    f+=-heapq.heappop(miss)
                if f<dist and not miss:
                    return -1
            heapq.heappush(miss,-gas)
            f-=dist
        return time 

