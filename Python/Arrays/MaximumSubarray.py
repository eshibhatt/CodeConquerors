#logic
''' 
1. We initialise a current sum, curr=arr[0]
and max_till_now = arr[0]
2. if curr sum is -ve, update it to 0
3. elif curr summ is +ve compare with max_till_now
4. When loop ends, output max_till_now
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        curr=nums[0]
        maxtill=nums[0]
        for i in range(1,len(nums)):
            if curr<0:
                curr=0
            curr+=nums[i]
            maxtill=max(maxtill,curr)
        return maxtill