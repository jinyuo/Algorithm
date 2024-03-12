import java.util.*;

class Main{
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int temp = num;
        int i = 1;
        
        while(num != cycle(temp)){
            i++;
            temp = cycle(temp);
        }
        System.out.println(i);
    }
    
    public static int cycle(int num){
        int ten = num / 10; //십의 자리
        int one = num % 10; //일의 자리
        int sum = ten + one;
        int result = (one * 10) + (sum % 10);
        
        return result;
    }
}