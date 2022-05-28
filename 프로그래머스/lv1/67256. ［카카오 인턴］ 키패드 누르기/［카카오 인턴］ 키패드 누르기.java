class Solution {
    public String solution(int[] numbers, String hand) {
        StringBuilder answer = new StringBuilder();
        char left = '*';
        char right = '#';
        for(int num : numbers){
            if(num % 3 == 1){
                answer.append("L");
                left = (char)(num + '0');
            }
            else if(num != 0 && num % 3 == 0){
                answer.append("R");
                right = (char)(num + '0');
            }
            else{
                int [][] location = {
                                        {3, 1}, 
                                        {0, 0}, {0, 1}, {0, 2}, 
                                        {1, 0}, {1, 1}, {1, 2},
                                        {2, 0}, {2, 1}, {2, 2},
                                        {3, 0}, {3, 2}
                                    };
                
                if(left == '*')
                    left = (char)(10 + '0');
                if(right == '#')
                    right = (char)(11 + '0');
                int lCnt = Math.abs(location[left - '0'][0] - location[num][0]) + Math.abs(location[left - '0'][1] - location[num][1]);
                int rCnt = Math.abs(location[right - '0'][0] - location[num][0]) + Math.abs(location[right - '0'][1] - location[num][1]);
                if(lCnt < rCnt){
                    answer.append("L");
                    left = (char)(num + '0');
                }else if(lCnt > rCnt){
                    answer.append("R");
                    right = (char)(num + '0');
                }else{
                    if(hand.equals("left")){
                        answer.append("L");
                        left = (char)(num + '0');
                    }else{
                        answer.append("R");
                        right = (char)(num + '0');
                    }
                }
            }
        }
        return answer.toString();
    }
}