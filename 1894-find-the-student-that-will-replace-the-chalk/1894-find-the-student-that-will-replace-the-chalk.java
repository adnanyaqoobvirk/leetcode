class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        long total = 0;
        for(int pieces : chalk)
            total += pieces;
        
        k %= total;
        for(int i = 0; i < chalk.length; i++){
            k -= chalk[i];
            if(k < 0)
                return i;
        }
        return 0;
    }
}