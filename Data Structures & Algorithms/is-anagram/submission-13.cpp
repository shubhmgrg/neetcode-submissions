class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> smap;
        map<char, int> tmap;

        for (char sc : s){
            if (!smap.contains(sc)){
                smap[sc] = 0;
            }
            smap[sc]++;
        }

        for (char tc : t){
            if (!tmap.contains(tc)){
                tmap[tc] = 0;
            }
            tmap[tc]++;
        }

        return smap == tmap;
    }
};
