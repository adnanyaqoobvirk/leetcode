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
    public void flatten(TreeNode root) {
        if(root != null){
            this.helper(root);
        }
    }
    
    private TreeNode[] helper(TreeNode curr){
        TreeNode tail = curr, left = curr.left, right = curr.right;
        
        if(left != null){
            TreeNode[] res = this.helper(left);
            tail.right = res[0];
            tail = res[1];
        }
        
        curr.left = null;
        
        if(right != null){
            TreeNode[] res = this.helper(right);
            tail.right = res[0];
            tail = res[1];
        }
        
        return new TreeNode[]{curr, tail};
    }
}