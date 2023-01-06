class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        cache={} #key=num : value= count
        
        for i in nums:
            if i in cache.keys():
                cache[i]+=1
            else:
                cache[i]=1
        
        a=list(cache.keys())
        for j in a:
            if cache[j]>int(n/2):
                return j
        return -1