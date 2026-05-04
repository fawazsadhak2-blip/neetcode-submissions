class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        
        for l in range(len(temperatures)):
            count=0
            for r in range(l + 1, len(temperatures)):
                if temperatures[r] > temperatures[l]:
                    count = r - l
                    break
            res.append(count)
        return res