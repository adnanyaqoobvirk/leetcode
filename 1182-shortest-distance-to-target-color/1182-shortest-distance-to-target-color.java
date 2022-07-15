class Solution {
    public List<Integer> shortestDistanceColor(int[] colors, int[][] queries) {
        ArrayList<Integer>[] colorIndices = new ArrayList[]{
            new ArrayList<Integer>(),
            new ArrayList<Integer>(),
            new ArrayList<Integer>()
        };
        for(int i = 0; i < colors.length; i++)
            colorIndices[colors[i] - 1].add(i);
        
        List<Integer> ans = new ArrayList<>();
        for(int i = 0; i < queries.length; i++){
            int idx = queries[i][0], color = queries[i][1];
            ArrayList<Integer> indices = colorIndices[color - 1];
            if(indices.size() == 0){
                ans.add(-1);
                continue;
            }
            
            int lo = 0, hi = indices.size() - 1;
            while(lo < hi){
                int mid = lo + (hi - lo) / 2;
                if(indices.get(mid) >= idx)
                    hi = mid;
                else
                    lo = mid + 1;
            }
            
            ans.add(
                Math.min(
                    Math.abs(indices.get(Math.max(lo - 1, 0)) - idx),
                    Math.abs(indices.get(lo) - idx)
                )
            );
        }
        return ans;
    }
}