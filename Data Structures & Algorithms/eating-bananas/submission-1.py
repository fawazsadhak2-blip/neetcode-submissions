class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        
        l = 1
        r = max(piles)
        ans = r
        
        while l <= r:
            mid = (l + r) // 2
            if mid == 0: 
                l = 1
                continue
            
            total_hours = 0
            for x in piles:
                total_hours += math.ceil(x / mid)
            
            if total_hours <= h:
                ans = mid          # valid, try smaller k
                r = mid - 1
            else:
                l = mid + 1        # too slow, increase k
        
        return ans