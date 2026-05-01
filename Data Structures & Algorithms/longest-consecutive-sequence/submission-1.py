class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        store=set(nums)

        for i in nums:
            if (i-1) not in store:
                streak=1
                while (i+streak) in store:
                    streak+=1
                res=max(res,streak)
        return res