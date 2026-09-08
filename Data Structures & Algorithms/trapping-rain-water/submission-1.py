class Solution:
    def trap(self, height: List[int]) -> int:
        rmax = height[-1]
        lmax = height[0]
        rp = len(height) - 1
        lp = 0
        water = 0

        while lp < rp:
            if rmax > lmax:
                water += lmax - height[lp]
                lp += 1
                lmax = max(height[lp], lmax)
            else:
                water += rmax - height[rp]
                rp -= 1
                rmax = max(height[rp], rmax)
        
        return water