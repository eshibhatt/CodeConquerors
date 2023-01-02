class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int count=0;
        if(nums.size()==1){
            return nums[0];
        }
        else{
        for(int i=1;i<nums.size();i++){
            if(nums[i]==nums[i-1]){
                count++;
                if(count>=(nums.size()/2)){
                    return nums[i];
                }
            }
            else{
                count=0;
            }
            
        }
        }
        return 0;
    }
};