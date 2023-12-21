import java.util.Stack;

class Solution {
    public int reverse(int x) {

        int MAXVALUE = (int)Math.pow(2,31) - 1;
        int MINVALUE = -(int)Math.pow(2,31);
        

        boolean isGreaterThan32Bit = x > MAXVALUE;
        boolean isSmallerThan32Bit = x < MINVALUE;


        if (isGreaterThan32Bit || isSmallerThan32Bit) {
            return 0;
        }


        Stack<Integer> digits = new Stack<>();
        
        while (x != 0) {
            int digit = x % 10;
            x = x / 10;
        
            digits.add(digit);
        }
    
        long multiplier = 1;
        long result = 0; 
        while (!digits.isEmpty()) {

            int digit = digits.pop();
            result += multiplier * digit;

            multiplier *= 10;
        }
    
        
        return (int)result;

    }
}