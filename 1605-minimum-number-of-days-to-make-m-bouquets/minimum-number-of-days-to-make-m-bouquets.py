class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        l=min(bloomDay)
        r=max(bloomDay)

        while l <= r :
            mid=(l+r)//2
            c=d=0
            for i in bloomDay:
                if i<=mid:
                    c+=1
                else:
                    d+=(c//k)
                    c=0
            d+=(c//k)
            if d>=(m):
                r=mid-1
            else:
                l=mid+1
        return(l)