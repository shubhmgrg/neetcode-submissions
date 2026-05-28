class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        if(prices.size() <= 1){
            return 0;
        }

        int l = 0;
        int r = 1;
        int maxprofit = 0;

        while(r < prices.size()){
            maxprofit = max(maxprofit, prices.at(r) - prices.at(l));
            cout << l << " r: " << r << "\n";
            if(prices.at(l) >= prices.at(r)){
                l = r;
            }
            r++;
        }

        return maxprofit;
    }
};
