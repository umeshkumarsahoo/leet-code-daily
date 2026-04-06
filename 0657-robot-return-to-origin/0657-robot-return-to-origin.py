class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y=0,0
        dir_list=moves.strip()
        for i in dir_list:
            if i=='U':y+=1
            elif i=='D':y-=1
            elif i=='R':x+=1
            else: x-=1
        return x==0 and y==0        