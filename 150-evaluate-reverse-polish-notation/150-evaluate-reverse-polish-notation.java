class Solution {
    public int evalRPN(String[] tokens) {
        ArrayList<String> stack = new ArrayList<>();
        for(String token : tokens){
            if (token.equals("+")){
                Integer op1 = Integer.parseInt(stack.remove(stack.size() - 1));
                Integer op2 = Integer.parseInt(stack.remove(stack.size() - 1));
                stack.add(Integer.toString(op1 + op2));
            } else if (token.equals("-")){
                Integer op1 = Integer.parseInt(stack.remove(stack.size() - 1));
                Integer op2 = Integer.parseInt(stack.remove(stack.size() - 1));
                stack.add(Integer.toString(op2 - op1));
            } else if (token.equals("*")){
                Integer op1 = Integer.parseInt(stack.remove(stack.size() - 1));
                Integer op2 = Integer.parseInt(stack.remove(stack.size() - 1));
                stack.add(Integer.toString(op1 * op2));
            } else if (token.equals("/")){
                Integer op1 = Integer.parseInt(stack.remove(stack.size() - 1));
                Integer op2 = Integer.parseInt(stack.remove(stack.size() - 1));
                stack.add(Integer.toString(op2 / op1));
            } else {
                stack.add(token);
            }
        }
        
        return Integer.parseInt(stack.remove(stack.size() - 1));
    }
}