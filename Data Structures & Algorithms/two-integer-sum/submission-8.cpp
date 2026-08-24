class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> sums;

        for (int i = 0; i < nums.size(); i++){
            if (sums.contains(nums.at(i))){
                return {sums[nums.at(i)], i};
            }
            sums[target - nums.at(i)] = i;
        }
    }
};
