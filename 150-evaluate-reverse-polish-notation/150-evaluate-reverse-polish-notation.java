class Solution {
    public int evalRPN(String[] tokens) {
        Set<String> special = new HashSet<>();
        special.add("+");
        special.add("-");
        special.add("*");
        special.add("/");
        
        ArrayList<String> stack = new ArrayList<>();
        for(String token : tokens){
            if(special.contains(token)){
                Integer op1 = Integer.parseInt(stack.remove(stack.size() - 1));
                Integer op2 = Integer.parseInt(stack.remove(stack.size() - 1));
                if (token.equals("+")){
                    stack.add(Integer.toString(op1 + op2));
                } else if (token.equals("-")){
                    stack.add(Integer.toString(op2 - op1));
                } else if (token.equals("*")){
                    stack.add(Integer.toString(op1 * op2));
                } else {
                    stack.add(Integer.toString(op2 / op1));
                }
            } else {
                stack.add(token);
            }
        }
        
        return Integer.parseInt(stack.remove(stack.size() - 1));
    }
}