#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zero=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0);
            zero++;
        }
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0){
                nums.erase(nums.begin()+i);
                nums.push_back(0);
                zero--;
                i--;
            }
            if(zero==0){
                break;
            }
        }
    }
};

int main(){
    cout<<"solved";
    return 0;
}