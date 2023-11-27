class Solution {
    public long solution(int a, int b) {       
//         long absAsum = (long)Math.abs(a) * (Math.abs(a) + 1) / 2;
//         long absBsum = (long)Math.abs(b) * (Math.abs(b) + 1) / 2;
        
//         if(a > 0 && b > 0){
//             if(a < b)
//                 return absBsum - absAsum + a;
//             else
//                 return absAsum - absBsum + b;
//         }else if(a < 0 && b > 0)
//             return absBsum - absAsum;
//         else if(a > 0 && b < 0)
//             return absAsum - absBsum;
//         else{
//             if(a < b)
//                 return -(absAsum - absBsum - b);
//             else
//                 return -(absBsum - absAsum - a);
//         }
        
        long start = a < b ? a : b;
        long end = a < b ? b : a;
            
        return (end - start + 1) * (end + start) / 2;
    }
}