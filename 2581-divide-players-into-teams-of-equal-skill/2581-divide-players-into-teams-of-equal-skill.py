class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill=sorted(skill)
        t_sum=skill[0]+skill[-1]
        t_chem=0
        for i in range(len(skill)//2):
            if (skill[i]+skill[-i-1])!=t_sum:
                return -1
            t_chem+=(skill[i]*skill[-i-1])
        return t_chem
with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(Solution().dividePlayers(nums),file=f)
exit(0)

        