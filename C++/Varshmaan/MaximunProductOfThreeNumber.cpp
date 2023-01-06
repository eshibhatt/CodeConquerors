class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int num=nums[0]*nums[1]*nums[nums.size()-1];
        int num1=nums[nums.size()-1]*nums[nums.size()-2]*nums[nums.size()-3];
        return (num>num1?num:num1);
    }
};