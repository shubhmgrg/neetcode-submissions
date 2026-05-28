class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> smap;
        map<char, int> tmap;

        if(s.size() != t.size()){
            return false;
        }
        
        for(int i = 0; i < s.size(); i++){
            if(smap.find(s[i]) ==  smap.end()){
                smap[s[i]] = 0;
            }
            smap[s[i]] += 1;
            if(tmap.find(t[i]) ==  tmap.end()){
                tmap[t[i]] = 0;
            }
            tmap[t[i]] += 1;
        }
        for (const auto& p : smap) {
            cout << p.first << " : " << p.second << '\n';
        }

        if(smap == tmap){
            return true;
        }
        return false;
        
    }
};
