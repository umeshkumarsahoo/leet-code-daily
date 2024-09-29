class AllOne:

    def __init__(self):
        self.dict={}

    def inc(self, key: str) -> None:
        if key  in self.dict:
            self.dict[key]+=1
        else:
            self.dict[key]=1
    def dec(self, key: str) -> None:
        if key in self.dict and self.dict[key]>1:
            self.dict[key]-=1
        else:
            self.dict.pop(key)
    def getMaxKey(self) -> str:
        if not self.dict:
            return ""
        max_val=max(self.dict.values())
        for key in self.dict.keys():
            if self.dict[key]==max_val:
                return key
    def getMinKey(self) -> str:
        if not self.dict:
            return ""
        min_val=min(self.dict.values())
        for key in self.dict.keys():
            if self.dict[key]==min_val:
                return key

        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()