import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        //초기값 설정
        int [][] st = {
                            {1,2,3,4,5}, 
                            {2,1,2,3,2,4,2,5},
                            {3,3,1,1,2,2,4,4,5,5}
                    };
        
        //맞은 개수 저장
        int [] cnt = new int[st.length];
        for(int i = 0; i < answers.length; i++)//문제 수만큼 반복
            for(int j = 0; j < st.length; j++)//학생 수만큼 반복
                if(answers[i] == st[j][i % st[j].length])
                    cnt[j]++;
        
        //최고 점수
        int maxScore = Math.max(cnt[0], Math.max(cnt[1], cnt[2]));
        
        //최고 점수에 해당하는 학생 저장
        List<Integer> list = new ArrayList<Integer>();
        for(int i = 0; i < 3; i++)
            if(cnt[i] == maxScore)
                list.add(i + 1);
    
        int [] answer = new int[list.size()];
        for(int i = 0; i < list.size(); i++)
            answer[i] = list.get(i);
        
        return answer;
    }
}