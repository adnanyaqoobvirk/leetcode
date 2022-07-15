class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int maxPile = 0;
        for(int pile : piles)
            maxPile = Math.max(maxPile, pile);
        
        int lo = 1, hi = maxPile;
        while(lo < hi){
            int mid = lo + (hi - lo) / 2;
            
            int hours = 0;
            for(int pile : piles)
                hours += (pile - 1) / mid + 1;
            
            if(hours > h)
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo;
    }
}