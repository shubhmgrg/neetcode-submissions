class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> buckets;
        for(int i = 0; i < strs.size(); i++){
            vector<int> numbers(26, 0);
            for(char c : strs[i]){
                numbers[c - 'a']++;
            }
            string s = to_string(numbers[0]);
            for(int i = 1; i < 26; i++){
                s += ',' + to_string(numbers[i]);
            }
            buckets[s].push_back(strs[i]);
        }
        vector<vector<string>> heheheha;
        for(const auto& a : buckets){
            heheheha.push_back(a.second);
        }
        return heheheha;
    }
};
