class Solution {
    public double average(int[] salary) {
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE, total = 0;
        for(int s : salary){
            min = Math.min(min, s);
            max = Math.max(max, s);
            total += s;
        }
        return (total - max - min) / (salary.length - 2.0);
    }
}