class Solution {
    public String solution(String s, int n) {
        StringBuilder answer = new StringBuilder();
        String [] strArr = s.split("");
        int cnt = (int)('z' - 'a') + 1;
        
        for(int i = 0; i < s.length(); i++){
            int temp = s.charAt(i);
            if(temp == 32)
                answer.append((char)temp);
            else if(temp >= (int)'A' && temp <= (int)'Z'){
                if(temp + n > (int)'Z')
                    answer.append((char)(temp + n - cnt));
                else
                    answer.append((char)(temp + n));
            }else if(temp >= (int)'a' && temp <= (int)'z'){
                if(temp + n > (int)'z')
                    answer.append((char)(temp + n - cnt));
                else
                    answer.append((char)(temp + n));
            }
        }
        return answer.toString();
    }
}