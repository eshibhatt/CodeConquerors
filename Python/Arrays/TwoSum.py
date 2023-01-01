class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache={}
        for i in range(0,len(nums)):
            diff=target-nums[i]
            if nums[i] in cache.keys():
                return(list([i,cache[nums[i]]]))
            else:
                cache[diff]=i