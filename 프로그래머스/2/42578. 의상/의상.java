import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> map = new HashMap<String, Integer>();
        
        for(int i = 0; i < clothes.length; i++){
            Integer num = map.getOrDefault(clothes[i][1], 1);
            map.put(clothes[i][1], ++num);
        }
        
        for(Map.Entry<String, Integer> entry : map.entrySet())
            answer *= entry.getValue();
        return answer - 1;
    }
}