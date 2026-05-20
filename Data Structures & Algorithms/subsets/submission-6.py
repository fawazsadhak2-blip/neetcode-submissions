class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subsets=[]

        def bt(i):
            if i==len(nums):
                res.append(subsets[:])
                return
            subsets.append(nums[i])
            bt(i+1)
            subsets.pop()
            bt(i+1)
        bt(0)
        return res