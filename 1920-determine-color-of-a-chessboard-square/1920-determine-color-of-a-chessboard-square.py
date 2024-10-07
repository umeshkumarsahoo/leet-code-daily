class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        dictionary={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
        sumi=dictionary[coordinates[0]]+int(coordinates[1])-1
        return 'false' if sumi%2==0 else 'true'
solution = Solution() 
with open("user.out", "w") as f:   
    inputs = map(loads, stdin)    
    for coordinates in inputs:       
        print(solution.squareIsWhite(coordinates), file=f)  
exit(0)  

