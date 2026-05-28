class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int> a = {};
        int l,r = 0;
        int maxi = 0;

        while(r < s.size()){
            if(a.find(s[r]) != a.end()){
                cout << "Hello";
                while(l <= a[s[r]]){
                    a.erase(s[l]);
                    l++;
                }
            }
            a[s[r]] = r;
            maxi = max(maxi, r - l + 1);
            r++;
        }

        return maxi;
    }
};
