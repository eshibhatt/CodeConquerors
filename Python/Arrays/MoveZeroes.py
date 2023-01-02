"""Algo
1. left & right ptr are initialised at 0
2. r is used to iterate, such that if the value at right ptr is 0 we increment r 
if its non-zero we swap the values of left and right ptr and increment both left 
and right ptr
3. note that left and right ptr denote the indices of the array which will be swapped"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l,r=0,0
        while r<len(nums):
            if nums[r]==0:
                r+=1
            else:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r+=1