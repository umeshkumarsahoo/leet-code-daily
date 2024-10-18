class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str=str(num)
        n=len(num_str)
        max_num=num
        for i in range(n):
            for j in range(i+1,n):
                num_list=list(num_str)
                num_list[i],num_list[j]=num_list[j],num_list[i]
                temp="".join(num_list)
                max_num=max(int(temp),max_num)
        return max_num
        