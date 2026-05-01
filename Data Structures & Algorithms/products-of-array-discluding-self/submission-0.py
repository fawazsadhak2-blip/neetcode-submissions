class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        pre=1
        post=1
        for i in range(len(nums)):
            result[i]=pre
            pre=pre*nums[i]
            
        for j in range(len(nums)-1,-1,-1):
            result[j]=result[j]*post
            post=post*nums[j]
        
        return result