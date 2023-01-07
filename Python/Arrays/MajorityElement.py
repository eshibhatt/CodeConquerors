class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        cache={} #key=num : value= count
        
        for i in nums: #keeping count of occurence of every element
            if i in cache.keys():
                cache[i]+=1
            else:
                cache[i]=1
        
        a=list(cache.keys()) #making a list of all distinct elements
        for j in a:
            if cache[j]>int(n/2): #we return the element whose count is greater than n/2
                return j
        return -1