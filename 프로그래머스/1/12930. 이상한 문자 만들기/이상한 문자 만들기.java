class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        int index = 0;
        
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) != ' '){
                if(index % 2 == 0)
                    sb.append(s.substring(i, i + 1).toUpperCase());
                else
                    sb.append(s.substring(i, i + 1).toLowerCase());
                index++;
            }
            else{
                index = 0;
                sb.append(" ");
            }
        }
        return sb.toString();
    }
}