/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> ans = new ArrayList<>();
        
        List<Node> q = new ArrayList<>();
        if(root != null){
            q.add(root);
        }
        
        while(q.size() > 0){
            List<Node> nq = new ArrayList<>();
            
            List<Integer> level = new ArrayList();
            for(Node node : q){
                level.add(node.val);
                
                for(Node child : node.children){
                    nq.add(child);
                }
            }
            q = nq;
            ans.add(level);
        }
        
        return ans;
    }
}