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
    int preorderIdx;
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorderIdx = 0;
        
        Map<Integer, Integer> inorderIdxMap = new HashMap<>();
        for(int i = 0; i < inorder.length; i++)
            inorderIdxMap.put(inorder[i], i);
        
        return helper(preorder, inorderIdxMap, 0, inorder.length - 1);
    }
    
    private TreeNode helper(int[] preorder, Map<Integer, Integer> inorderIdxMap, int left, int right){
        if(left > right)
            return null;
        
        int rootIdx = inorderIdxMap.get(preorder[this.preorderIdx]);
        TreeNode root = new TreeNode(preorder[this.preorderIdx++]);
        
        root.left = helper(preorder, inorderIdxMap, left, rootIdx - 1);
        root.right = helper(preorder, inorderIdxMap, rootIdx + 1, right);
        
        return root;
    }
}