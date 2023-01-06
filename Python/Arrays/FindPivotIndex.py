class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #we initialise l as 0 & r as total
        leftSum, rightSum = 0, sum(nums)
        for i in range(0,len(nums)):
            rightSum -= nums[i] #in every iteration we decrement the current element from r
            if leftSum == rightSum:
                return i
            leftSum += nums[i] #in every iteration we increment the current element to l
        return -1
