class Vector2D {
    private int[][] vec;
    private int v;
    private int i;
    
    public Vector2D(int[][] vec) {
        this.vec = vec;
    }
    
    public int next() {
        int ans = this.vec[this.v][this.i];
        if(this.i == this.vec[this.v].length - 1){
            this.v++;
            this.i = 0;
        } else {
            this.i++;
        }
        return ans;
    }
    
    public boolean hasNext() {
        while(this.v < this.vec.length && this.vec[this.v].length == 0){
            this.v++;
        }
        
        if(this.v < this.vec.length && this.i < this.vec[this.v].length){
            return true;
        } else {
            return false;
        }
    }
}

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D obj = new Vector2D(vec);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */