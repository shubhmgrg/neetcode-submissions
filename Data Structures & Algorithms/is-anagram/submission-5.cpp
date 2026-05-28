class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> word1;
        map<char, int> word2;

        for(char b : s){
            word1[b]++;
        }

        for(char a : t){
            word2[a]++;
        }

        return word1 == (word2);
    }
};
