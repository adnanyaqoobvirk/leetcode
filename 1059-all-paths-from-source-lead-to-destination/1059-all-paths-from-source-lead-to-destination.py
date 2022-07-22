class Solution {
    public boolean leadsToDestination(int n, int[][] edges, int source, int destination) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for(int[] edge : edges){
            int src = edge[0], dst = edge[1];
            if(!graph.containsKey(src)){
                graph.put(src, new ArrayList<>());
            }
            graph.get(src).add(dst);
        }
        
        return this.helper(new HashMap<>(), graph, destination, source);
    }
    
    private boolean helper(
        Map<Integer, Integer> nodeColor, 
        Map<Integer, List<Integer>> graph, 
        int destination, 
        int curr
    ){
        if(nodeColor.containsKey(curr)){
            return nodeColor.get(curr) == 1;
        }
        
        if(!graph.containsKey(curr)){
            if(curr != destination){
                return false;
            }
            else {
                nodeColor.put(curr, 1);
                return true;
            }
        }
        
        nodeColor.put(curr, 0);
        for(int child : graph.get(curr)){
            if(!this.helper(nodeColor, graph, destination, child)){
                return false;
            }
        }
        nodeColor.put(curr, 1);
        
        return true;
    }
}