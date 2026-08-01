class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        maxi=0
    

        while l<r:
            n=r-l
            sol=n*(min(height[l],height[r]))
            maxi=max(maxi,sol)
            if height[l]> height[r]:
                r-=1
            else:
                l+=1
        return maxi
        """
        :type height: List[int]
        :rtype: int
        """
        