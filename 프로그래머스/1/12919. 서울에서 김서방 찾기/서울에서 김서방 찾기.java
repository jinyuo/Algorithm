class Solution {
    public String solution(String[] seoul) {
        StringBuilder answer = new StringBuilder();
        answer.append("김서방은 ");
        
        for(int i = 0; i < seoul.length; i++){
            if(seoul[i].equals("Kim")){
                answer.append(i + "에 있다");
                break;
            }
        }
        
        return answer.toString();
    }
}