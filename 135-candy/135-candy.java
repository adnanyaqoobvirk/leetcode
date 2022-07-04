class Solution {
    public int candy(int[] ratings) {
        int candies[] = new int[ratings.length];
        candies[0] = 1;
        
        for(int i = 1; i < ratings.length; i++){
            candies[i] = 1;
            if(ratings[i] > ratings[i - 1])
                candies[i] = candies[i - 1] + 1;
        }
        
        int ans = candies[ratings.length - 1];
        for(int i = ratings.length - 2; i >= 0; i--){
            if(ratings[i] > ratings[i + 1])
                candies[i] = Math.max(candies[i], candies[i + 1] + 1);
            ans += candies[i];
        }
        
        return ans;
    }
}