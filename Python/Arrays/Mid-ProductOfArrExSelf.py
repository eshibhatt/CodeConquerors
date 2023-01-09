#Brute
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in range(0,len(nums)):
            multi=1
            for j in range(0,len(nums)):
                if j!=i:
                    multi*=nums[j]
            answer.append(multi)
        return answer

#optimised
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n  #answer[i]=prefix[i]*postfix[i]
        
        prefix = 1
        for i in range(0,n):
            answer[i]=prefix #multiplies till last no
            prefix *= nums[i] #then updates for next iter
            
        postfix = 1
        for i in range(n-1,-1,-1): #revRange n-1 to -1 excluded, step -1
            answer[i]*= postfix
            postfix *=nums[i]
        return answer