import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        // 인덱스에 해당하는 스테이지에서 막힌 사람의 수
        int [] playStages = new int[N];
        
        for(int stage : stages)
            if(stage <= N) // 플레이 중인 스테이지가 스테이지 개수보다 큰 유저 제외
                playStages[stage - 1]++;
        
        // 인덱스에 해당하는 스테이지 당 실패율 계산
        int sum = stages.length; // 전체 유저 수
        List<Double> list = new ArrayList<Double>();
        for(int i = 0; i < N; i++){
            list.add((double)playStages[i] / sum);
            sum -= playStages[i]; // 해당 스테이지에서 막힌 유저 제외
            
            if(sum <= 0) // 여기부터
                break;
        }
        for(int i = list.size(); i < N; i++)
            list.add(0.0);
        // 여기까지 전체 유저 수가 0 이하로 갈 때 처리
        
        int [] answer = new int [N];
        int i = 0;
        while(i < N){
            double max = Collections.max(list);
            int index = list.indexOf(max);
            answer[i++] = index + 1;
            list.set(index, -1.0);
        }
        
        return answer;
    }
}