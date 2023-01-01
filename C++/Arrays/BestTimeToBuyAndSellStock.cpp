#include<iostream>
#include<vector>
#include<climits>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit=0;
        int dip=INT_MAX;
        int op=0;
        for(int i=0;i<prices.size();i++){
            if(prices[i]<dip){
                dip=prices[i];
            }
            profit = prices[i]-dip;
            if(op<profit){
                op=profit;
            }
        }
        return op;
    }
};

int main(){
    cout<<"solved";
    return 0;
}