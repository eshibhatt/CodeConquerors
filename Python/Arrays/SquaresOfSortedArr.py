#brute
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums):
            nums[i]=nums[i]**2 #turning into square & putting in place
            i+=1
        nums.sort() #then sorting it
        return nums
        