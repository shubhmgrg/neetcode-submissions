class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> dups;
        for(int i : nums){
            if(dups.find(i) != dups.end()){
                return true;
            }
            dups.insert(i);
        }
        return false;
    }
};