class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> mymap;

        for (int num : nums){
            if(!mymap.contains(num)){
                mymap[num] = 0;
            }
            mymap[num]++;
        }
        int size = nums.size();

        vector<vector<int>> buckets(size + 1);
        for (auto freq : mymap){
            buckets[freq.second].push_back(freq.first);
        }

        int count = 0;
        vector<int> results;

        for (int i = size; i >= 0; i--){
            if (count >= k) {
                return results;
            }
            for (int num : buckets.at(i)){
                results.push_back(num);
                count++;
            }
        }
        return results;
    }
};
