class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        dictionary={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
        sumi=dictionary[coordinates[0]]+int(coordinates[1])-1
        return False if sumi%2==0 else True


