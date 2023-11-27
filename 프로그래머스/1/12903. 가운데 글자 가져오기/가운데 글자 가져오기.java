class Solution {
    public String solution(String s) {       
        int start = s.length() / 2;
        if(s.length() % 2 == 0)
            return s.substring(start - 1, start + 1);
        else
            return s.substring(start, start + 1);
    }
}