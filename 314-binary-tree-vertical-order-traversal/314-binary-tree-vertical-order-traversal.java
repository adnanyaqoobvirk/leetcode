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
class NodeColumn {
    public TreeNode node;
    public int col;
    
    NodeColumn(TreeNode node, int col){
        this.node = node;
        this.col = col;
    }
}

class Solution {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        if(root == null){
            return new ArrayList<List<Integer>>();
        }
        
        Map<Integer, List<Integer>> colValues = new HashMap<>();
        
        List<NodeColumn> q = new ArrayList<>();
        q.add(new NodeColumn(root, 0));
        
        int minCol = Integer.MAX_VALUE, maxCol = Integer.MIN_VALUE;
        while(q.size() > 0){
            List<NodeColumn> nq = new ArrayList<>();
            for(NodeColumn nc : q){
                if(!colValues.containsKey(nc.col)){
                    colValues.put(nc.col, new ArrayList<>());
                }
                colValues.get(nc.col).add(nc.node.val);
                minCol = Math.min(minCol, nc.col);
                maxCol = Math.max(maxCol, nc.col);
                
                if(nc.node.left != null){
                    nq.add(new NodeColumn(nc.node.left, nc.col - 1));
                }
                
                if(nc.node.right != null){
                    nq.add(new NodeColumn(nc.node.right, nc.col + 1));
                }
            }
            q = nq;
        }
        
        List<List<Integer>> ans = new ArrayList<>();
        for(int i = minCol; i <= maxCol; ++i){
            ans.add(colValues.get(i));
        }
        return ans;
    }
}