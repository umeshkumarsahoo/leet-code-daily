class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n=len(tasks)
        tasks=sorted([(t[0],t[1],i) for i,t in enumerate(tasks)])
        i=0
        h=[]
        res=[]
        time=tasks[0][0]
        while len(res)<len(tasks):
            while (i<len(tasks)) and tasks[i][0]<=time:
                heapq.heappush(h,(tasks[i][1],tasks[i][2]))
                i+=1
            if h:
                t_diff,orig=heapq.heappop(h)
                time+=t_diff
                res.append(orig)
            elif i<len(tasks):
                time=tasks[i][0]
        return res

