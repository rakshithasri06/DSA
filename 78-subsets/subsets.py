class Solution(object):
    def subsets(self, nums):
        result=[]

        def backtracking(index,path):
            if index==len(nums):
                result.append(path[:])
                return
            
            path.append(nums[index])
            backtracking(index+1,path)
            path.pop()

            backtracking(index+1,path)
        
        backtracking(0,[])
        return result
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        