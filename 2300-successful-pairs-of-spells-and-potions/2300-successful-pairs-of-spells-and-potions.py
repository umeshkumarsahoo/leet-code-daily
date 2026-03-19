class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        def search(arr, n, s):
            start, end = 0, len(arr) - 1
            idx = len(arr)  
            
            while start <= end:
                mid = (start + end) // 2
                
                if arr[mid] * n >= s:
                    idx = mid
                    end = mid - 1 
                else:
                    start = mid + 1
            
            return len(arr) - idx

        potions.sort()
        ans = []
        
        for n in spells:
            ans.append(search(potions, n, success))
        
        return ans