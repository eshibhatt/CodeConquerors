class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums ==[]:
            return 0
        i,j=0,1 #initialising 2 ptrs
        n=len(nums)
        while j<n: #using j for traversal
            if nums[i]!=nums[j]:
                if j!=i+1:
                    nums[i+1]=nums[j]
                i+=1
            j+=1
        return i+1