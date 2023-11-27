import java.util.*;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        int loopSize = arr1.length;
        String [] answer = new String[loopSize];
        
        for(int i = 0; i < loopSize; i++){
            answer[i] = Integer.toBinaryString(arr1[i] | arr2[i]);
            
            // 문자열 길이 맞춤
            for(int j = answer[i].length(); j < loopSize; j++)
                answer[i] = "0" + answer[i];
            
            answer[i] = answer[i].replaceAll("0", " ");
            answer[i] = answer[i].replaceAll("1", "#");
        }
        return answer;
    }
}