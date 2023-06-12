import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Integer> qu = new LinkedList<Integer>();
        
        for(int num : priorities)
            qu.add(num);

        while(!qu.isEmpty()){
            if(qu.peek() == Collections.max(qu)){
                qu.poll();
                ++answer;
                if(--location < 0)
                    break;
            } else{
                qu.add(qu.poll());
                location = location == 0 ? qu.size() - 1 : --location;
            }
        }
        return answer;
    }
}