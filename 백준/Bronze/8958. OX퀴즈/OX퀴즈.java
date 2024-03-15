/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(br.readLine());
		String str;
		for(int i = 0; i < testCase; i++){
			str = br.readLine();
			int sum = 0;
			int seq = 0;
			for(int j = 0; j < str.length(); j++){
				if(str.charAt(j) == 'O')
					sum += ++seq;
				else
					seq = 0;
			}
			System.out.println(sum);
		}
		
	}
}