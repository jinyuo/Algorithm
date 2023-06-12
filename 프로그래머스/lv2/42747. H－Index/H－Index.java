import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int n = citations.length; // 논문 편수
        Arrays.sort(citations);
        int h = n < citations[0] ? n : citations[0]; // 최소 인용 횟수
        
        while(h <= citations[citations.length - 1]){
            int less = 0;
            for(int i = 0; i < citations.length; i++){
                if(citations[i] >= h){
                    less = i;
                    break;
                }
            }
            int more = n - less;
                        
            if(more >= h && less <= h && answer < h)
                answer = h;
            h++;
        }
        return answer;
    }
}