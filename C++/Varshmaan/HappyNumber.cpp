class Solution {
public:
    bool isHappy(int n) {
        int temp=n;
        int sum=0;
        while(sum!=1){
            sum=0;
            while(temp>0){
                sum+=pow((temp%10),2);
                temp/=10;
            }
            if(sum == 4){
                return false;
            }
            temp=sum;
        }
        return true;
    }
}