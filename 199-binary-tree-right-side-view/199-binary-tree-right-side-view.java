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
    public List<Integer> rightSideView(TreeNode root) {
        ArrayList<Integer> ans = new ArrayList<>();
        
        if(root == null)
            return ans;
        
        ArrayList<TreeNode> q = new ArrayList<>();
        q.add(root);
        
        while(q.size() > 0){
            ans.add(q.get(q.size() - 1).val);
            
            ArrayList<TreeNode> nq = new ArrayList<>();
            for(int i = 0; i < q.size(); i++){
                TreeNode curr = q.get(i);
                if(curr.left != null)
                    nq.add(curr.left);
                if(curr.right != null)
                    nq.add(curr.right);
            }
            q = nq;
        }
        
        return ans;
    }
}