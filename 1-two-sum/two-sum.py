class Solution():
    def twoSum(self, nums, target):
        dic={}
        for i,num in enumerate(nums):
            comp=target-num
            if comp in dic:
                return(dic[comp],i)
            else:
                dic[num]=i

