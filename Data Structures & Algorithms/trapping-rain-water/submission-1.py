class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res=0
        lmax=height[l]         
        rmax=height[r]

        while l<r:
            if (height[l]<height[r]):
                lmax=max(lmax,height[l])
                if (lmax-height[l]>0):
                    res+=lmax-height[l]
                l+=1
            else:
                rmax=max(rmax,height[r])
                if (rmax-height[r]>0):
                    res+=rmax-height[r]
                r-=1
        return res
            