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
    public List<List<Integer>> levelOrder(TreeNode root) {
        ArrayList<List<Integer>> ans = new ArrayList<>();
        if(root == null)
            return ans;
        
        ArrayList<TreeNode> q = new ArrayList<>();
        q.add(root);
        while(q.size() > 0){
            ArrayList<TreeNode> nq = new ArrayList<>();
            ArrayList<Integer> level = new ArrayList<>();
            
            for(TreeNode curr : q){
                level.add(curr.val);
                
                if(curr.left != null)
                    nq.add(curr.left);
                
                if(curr.right != null)
                    nq.add(curr.right);
            }
            
            q = nq;
            ans.add(level);
        }
        
        return ans;
    }
}