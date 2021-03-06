/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
};
*/

class Solution {
    public Node inorderSuccessor(Node node) {
        if(node.right != null){
            Node curr = node.right;
            while(curr.left != null)
                curr = curr.left;
            return curr;
        }
        
        while(node.parent != null && node.parent.right == node)
            node = node.parent;
        return node.parent;
    }
}