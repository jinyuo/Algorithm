import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int cnt = 0;
        int [] answer = new int[arr.length];
        
        for(int i = 0; i < arr.length - 1 ; i++)
            if(arr[i] != arr[i + 1])
                answer[cnt++] = arr[i];
            
        answer[cnt++] = arr[arr.length - 1];
        return Arrays.copyOf(answer, cnt);
    }
    
}