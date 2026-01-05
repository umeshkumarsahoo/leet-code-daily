class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start=0
        end=len(letters)-1
        while start<=end:
            middle=(start+end)//2
            if ord(letters[middle])>ord(target):
                end=middle-1
            else:
                start=middle+1
        # if ord(target)>ord(letters[middle]):
        #     return letters[0]
        # else :
        #     return letters[middle]
        return letters[start % len(letters)]
        