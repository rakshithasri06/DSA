class Solution(object):
    def maxArea(self, height):
        res=0
        l=0
        r=len(height)-1
        while l<r:
            total=min(height[l],height[r]) * (r-l)
            res=max(res,total)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return (res)

  