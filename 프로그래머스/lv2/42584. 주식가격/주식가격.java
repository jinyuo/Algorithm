import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        for(int i = 0; i < prices.length; i++){
            for(int j = i + 1; j < prices.length; j++){
                if(prices[i] > prices[j] || j == prices.length - 1){
                    //System.out.printf("price[%d] = %d, price[%d] = %d\n", i, prices[i], j, prices[j]);
                    answer[i] = j - i;
                    break;
                }
                
            }
        }
        //System.out.println(Arrays.toString(answer));
        return answer;
    }
}