import java.util.*;

class Solution {
    public long solution(long n) {
        String num = Long.toString(n);
        String [] array = num.split("");
        StringBuilder sb = new StringBuilder();
        
        Arrays.sort(array, Collections.reverseOrder());
        
        for(int i = 0; i < array.length; i++)
            sb.append(array[i]);
        
        return Long.parseLong(sb.toString());
    }
}