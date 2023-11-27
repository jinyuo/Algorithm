import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> list = new ArrayList<Integer>();
        int [] answer = {};
        for(int num : arr){
            if(num % divisor == 0)
                list.add(num);
        }
        int size = list.size();
        if(size == 0){
            answer = new int[1];
            answer[0] = -1;
        }
        else{
            answer = new int[size];
            for(int i = 0; i < size; i++){
                int min =  Collections.min(list);
                answer[i] = min;
                list.remove((Integer)min);
            }
        }

        return answer;
    }
}