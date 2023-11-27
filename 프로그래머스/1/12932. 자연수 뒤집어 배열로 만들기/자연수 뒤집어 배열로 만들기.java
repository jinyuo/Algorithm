class Solution {
    public int[] solution(long n) {
        int[] answer = {};
        String s = Long.toString(n);
        int length = s.length();
        answer = new int[length];
        for(int i = 0; i < length; i++)
            answer[i] = Integer.parseInt(String.valueOf(s.charAt(length - 1 - i)));
        return answer;
    }
}