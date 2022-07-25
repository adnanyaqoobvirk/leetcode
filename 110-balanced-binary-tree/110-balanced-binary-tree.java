/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        int ans = this.helper(root);
        return ans > -1;
    }
    
    private int helper(TreeNode curr) {
        if(curr == null){
            return 0;
        }
        
        int left = this.helper(curr.left);
        int right = this.helper(curr.right);
        
        if(left == -1 || right == -1 || Math.abs(right - left) > 1){
            return -1;
        } else {
            return Math.max(left, right) + 1;
        }
    }
}