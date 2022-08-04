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
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        this.helper(root, ans);
        return ans;
    }
    
    private int helper(TreeNode curr, List<List<Integer>> ans){
        if(curr == null){
            return 0;
        }
        
        int left = this.helper(curr.left, ans);
        int right = this.helper(curr.right, ans);
        
        int i = Math.max(left, right);
        if(i > ans.size() - 1){
            ans.add(new ArrayList<>());
        }
        
        ans.get(i).add(curr.val);
        
        return i + 1;
    }
}