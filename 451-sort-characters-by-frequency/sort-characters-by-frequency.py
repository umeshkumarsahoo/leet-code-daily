class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        sorted_list = sorted(dic.items(), key=lambda item: item[1], reverse=True)
        l = [k * x for k, x in sorted_list]
        return "".join(l)