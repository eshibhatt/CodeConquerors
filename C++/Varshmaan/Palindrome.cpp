class Solution {
public:
    bool isPalindrome(int x) {
        double palindrome=0;
        int temp = x;
        while(temp>0){
            palindrome=(palindrome*10)+(temp%10);
            temp=temp/10;
        }
        cout<<palindrome;
        return (palindrome==x?true:false);
    }
};