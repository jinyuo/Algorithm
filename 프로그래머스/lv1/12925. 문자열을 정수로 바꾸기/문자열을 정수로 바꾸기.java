class Solution {
    public int solution(String s) {
        int answer = Integer.parseInt(s);
        
//         if(s.charAt(0) == '-' || s.charAt(0) == '+'){
//             String [] oper = s.split("\\"+ Character.toString(s.charAt(0)));
//             answer = trans(oper[1]);
            
//             if(s.charAt(0) == '-')
//                 answer = -1 * answer;
//         }else
//             answer = trans(s);
         return answer;
    
     }
    
//     public int trans(String s){
//         int sum = 0;
//         for(int i = 0; i < s.length(); i++)
//             sum += Integer.parseInt(Character.toString(s.charAt(i))) * Math.pow(10, s.length() - i - 1);
        
//         return sum;
//     }
}