import java.util.*;

class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        int [] score = new int [3];
        int opp = -1; // 기회
        for(int i = 0; i < dartResult.length(); i++){
            if(i < dartResult.length() - 2 && dartResult.substring(i, i + 2).equals("10")){
                score[++opp] = Integer.parseInt(dartResult.substring(i, i + 2));
                ++i;
            }else{
                switch(dartResult.charAt(i)){
                    case 'S':
                        score[opp] = (int)Math.pow(score[opp], 1);
                        break;
                    case 'D':
                        score[opp] = (int)Math.pow(score[opp], 2);
                        break;
                    case 'T':
                        score[opp] = (int)Math.pow(score[opp], 3);
                        break;
                    case '*':
                        int loop = opp - 1 < 0 ? opp : opp - 1;
                            
                        for(int j = loop; j <= opp; j++)
                            score[j] *= 2;
                        break;
                    case '#':
                        score[opp] = -1 * score[opp];
                        break;
                    default :
                        score[++opp] = Integer.parseInt(dartResult.substring(i, i + 1));
                        break;
                }
            }
                
        }

        for(int i = 0; i < score.length; i++)
            answer += score[i];
        return answer;
    }
}