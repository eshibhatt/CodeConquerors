class Solution(object):
    def runningSum(self, nums):
        stat=0
        i=0
        while i<len(nums):
            stat+=nums[i] #we add the element per iteration
            nums[i] = stat #edit it to the array in-place
            i += 1
        return nums #return the given array