import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        String [] array = s.split("");
        Arrays.sort(array, Collections.reverseOrder());
        
        for(int i = 0; i < array.length; i++)
            answer.append(array[i]);
        return answer.toString();
    }
}