class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int rsum=0,lsum=0,sum=0;
        sum=accumulate(nums.begin(),nums.end(),0);
        rsum=sum;
        for(int i=0;i<nums.size();i++){
            rsum=rsum-nums[i];
            if(rsum==lsum){
                return i;
            }
            lsum+=nums[i];
        }  
        return -1;
    }
};