class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<string> sorted;
        for (string str : strs){
            string s = str;
            sort(s.begin(), s.end());
            sorted.push_back(s);
            cout << s << "\n";
        }
        map<string, vector<string>> groups;
        for (int i = 0; i < sorted.size(); i++){
            groups[sorted.at(i)].push_back(strs.at(i));
        }
        vector<vector<string>> result;
        for (auto group : groups){
            result.push_back(group.second);
        }
        return result;
    }
};
