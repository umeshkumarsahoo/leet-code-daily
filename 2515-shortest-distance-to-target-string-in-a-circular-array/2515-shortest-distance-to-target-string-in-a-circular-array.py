class Solution:
   def closestTarget(self, words, target, startIndex):
        n = len(words)
        dist = float('inf')

        for i in range(n):
            if words[i] == target:
                d = abs(i - startIndex)
                dist = min(dist, min(d, n - d))

        return -1 if dist == float('inf') else dist