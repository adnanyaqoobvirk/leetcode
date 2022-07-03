class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int[] ans = new int[nums.length];
        int j = 0; 
        
        int pcount = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] < pivot){
                ans[j] = nums[i];
                j++;
            }
            else if (nums[i] == pivot){
                pcount++;
            }
        }
        
        for (int i = 0; i < pcount; i++){
            ans[j] = pivot;
            j++;
        }
        
        for (int i = 0; i < nums.length; i++){
            if (nums[i] > pivot){
                ans[j] = nums[i];
                j++;  
            }
        }
        
        return ans;
    }
}