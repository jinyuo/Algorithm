import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int [] endDay = new int [progresses.length];
        List<Integer> list = new ArrayList<Integer>();
        
        for(int i = 0; i < progresses.length; i++)
            endDay[i] = (int)Math.ceil((100.0 - progresses[i]) / speeds[i]);        
        System.out.println(Arrays.toString(endDay));
        for(int i = 0; i < progresses.length; i++){
            int deploy = 0;
            int cnt = 0;
            
            if(endDay[i] > 0){
                deploy = endDay[i];
                endDay[i] = -1;
                cnt++;
            }else 
                continue;
            
            for(int j = i + 1; j < progresses.length; j++)
                if(endDay[j] <= deploy && endDay[j] > 0){
                    cnt++;
                    endDay[j] = -1;
                }else if(endDay[j] > deploy)
                    break;
            list.add(cnt);    
        }
        System.out.println(list);
        int[] answer = new int[list.size()];
        for(int i = 0; i < list.size(); i++)
            answer[i] = list.get(i);
        
        return answer;
    }
}