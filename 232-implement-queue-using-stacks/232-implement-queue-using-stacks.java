class MyQueue {
    private Stack<Integer> s1, s2;
    private Integer front;

    public MyQueue() {
        this.s1 = new Stack<>();
        this.s2 = new Stack<>();
        this.front = null;
    }
    
    public void push(int x) {
        if(this.front == null)
            this.front = x;
        
        this.s1.push(x);
    }
    
    public int pop() {
        
        while(this.s1.size() > 1){
            this.s2.push(this.s1.pop());
            if(this.front == null)
                this.front = this.s2.peek();
        }
        int res = this.s1.pop();
        this.front = null;
        while(this.s2.size() > 0){
            this.s1.push(this.s2.pop());
            if(this.front == null)
                this.front = this.s1.peek();
        }
        return res;
    }
    
    public int peek() {
        return this.front;
    }
    
    public boolean empty() {
        return this.s1.size() == 0 ? true : false;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */