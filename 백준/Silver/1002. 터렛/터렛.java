/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Main
{
	public static void main (String[] args)	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		int testCase = sc.nextInt();
		
		for(int i = 0; i < testCase; i++){
			int x1 = sc.nextInt();
			int y1 = sc.nextInt();
			int r1 = sc.nextInt();
			int x2 = sc.nextInt();
			int y2 = sc.nextInt();
			int r2 = sc.nextInt();
			double dist = Math.sqrt(Math.pow(x2 - x1,2) + Math.pow(y2 - y1,2));
			
            if(dist == 0){
                if(r1 == r2)
                    System.out.println(-1);
                else
                    System.out.println(0);
            }else{
                if(Math.abs(r1-r2) < dist && dist < r1+r2)
                    System.out.println(2);
                else if(dist == r1 + r2 || dist == Math.abs(r1-r2))
				    System.out.println(1);
                else if(dist > r1 + r2 || dist < Math.abs(r1-r2))
                    System.out.println(0);
            }
        }
    }
}