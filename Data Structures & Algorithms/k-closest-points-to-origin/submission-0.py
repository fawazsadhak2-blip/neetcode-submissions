class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        for x,y in points:
            dist=((x**2)+(y**2))
            minheap.append([dist,x,y])
        heapq.heapify(minheap)

        res=[]
        while k>0:
            d,a,b=heapq.heappop(minheap)
            res.append([a,b])
            k-=1
        return res


        