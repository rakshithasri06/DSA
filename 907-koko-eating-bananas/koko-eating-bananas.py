class Solution(object):
    def minEatingSpeed(self, piles, h):
        l=1
        r=max(piles)
        res=r
        while l<=r:
            mid=(l+r)//2
            hrs=0
            for p in piles:
                hrs+=math.ceil(p/float(mid))
            if hrs<=h:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return (int(res))
                
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        