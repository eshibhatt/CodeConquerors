class Solution {
public:
    int minMoves(vector<int>& nums) {
        int difference=nums[0];
        int sum=0;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size();i++){
            sum+=nums[i]-nums[0];
        }
        return sum;
    }
};