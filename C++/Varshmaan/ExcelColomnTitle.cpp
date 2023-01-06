class Solution {
public:
    string convertToTitle(int columnNumber) {
        string s={""};
        while(columnNumber){
        columnNumber--;
            s+=char((columnNumber%26)+65);
            columnNumber/=26;
        }
        reverse(s.begin(),s.end());
        return s;
    }
};