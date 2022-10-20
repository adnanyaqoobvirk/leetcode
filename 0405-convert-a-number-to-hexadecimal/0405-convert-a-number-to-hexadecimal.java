class Solution {
    public String toHex(int num) {
        String HEX_CHARS = "0123456789abcdef";
        
        StringBuilder sb = new StringBuilder();
        do {
            sb.append(HEX_CHARS.charAt(num & 0xf));
            num >>>= 4;
        } while (num != 0);
        
        return sb.reverse().toString();
    }
}