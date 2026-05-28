class Solution {
public:
    int characterReplacement(string s, int k) {
        map<char, int> count;
        int res = 0;

        int l = 0, maxl = 0;

        for(int r = 0; r < s.size(); r++){
            count[s[r]]++;
            maxl = max(maxl, count[s[r]]);

            while((r - l + 1) - maxl > k){
                count[s[l]]--;
                l++;
            }

            res = max(res, r - l + 1);
        }

        return res;
    }
};
