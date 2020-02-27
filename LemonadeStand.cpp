class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int five = 0;
        int ten = 0;

        for(auto w: bills)
        {
            if(w == 5) ++five;
                else if(w == 10) {
                    if (not five) return false;
                    --five; ++ten;
                    }
            else {
                if(ten > 0 and five > 0) {
                    --ten; --five;
                }
                else if (five > 2) {
                    five -= 3;
                }
                else return false;
            }


        }
        return true;
    }
};