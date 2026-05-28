class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int n : nums){
            count[n] = 1 + count[n];
        }

        vector<vector<int>> freq(nums.size() + 1);
        for(const auto& p : count){
            freq[p.second].push_back(p.first);
        }
        vector<int> res;
        int l = 0;
        for(int i = freq.size() - 1; i > 0; i--){
            if(l == k){
                break;
            }
            for(int j = 0; j < freq[i].size(); j++){
                res.push_back(freq[i][j]);
                l++;
                if(l == k){
                    break;
                }
            }
        }
        return res;
    }
};
