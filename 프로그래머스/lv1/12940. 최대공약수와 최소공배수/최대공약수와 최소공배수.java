class Solution {
    public int[] solution(int n, int m) {
        int gcd = gcd(n, m);
        int lcm = n * m / gcd;
        int[] answer = {gcd, lcm};
        return answer;
    }
    
     public int gcd(int p, int q){
         return q == 0 ? p : gcd(q, p%q);
    }
}