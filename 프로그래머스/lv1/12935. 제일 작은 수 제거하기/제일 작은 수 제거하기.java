import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> list = new ArrayList<Integer>();
        
        for(int num : arr)
            list.add(num);
        
        list.remove(Collections.min(list));
        int [] answer = {};
        if(list.size() == 0){
            answer = new int [1];
            answer[0] = -1;
        }else{
            answer = new int[list.size()];
            for(int i = 0; i < list.size(); i++)
                answer[i] = list.get(i);
        }
        
        return answer;
    }
}