class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> uniques = {};
        for (int num : nums){
            if(uniques.contains(num)) {
                return true;
            } else {
                uniques.insert(num);
            }
        }
        return false;
    }
};