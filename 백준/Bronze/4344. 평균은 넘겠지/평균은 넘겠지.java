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
		int testCase = Integer.parseInt(br.readLine());// 첫 번째 줄
		String str;
		
		for(int i = 0; i < testCase; i++){
			str = br.readLine();
			String [] arr = str.split(" ");
			int stu = Integer.parseInt(arr[0]);//학생 수
			int sum = 0;//점수 합
			for(int j = 1; j <= stu; j++)
				sum += Integer.parseInt(arr[j]);
			
			double avg = (double)sum / stu;//평균 점수
			
			sum = 0;//평균 이상 학생 수
			for(int j = 1; j <= stu; j++)
				if(Integer.parseInt(arr[j]) > avg)
					sum++;
			
			double ratio = (double)sum / stu * 100;//평균 이상 학생 비율
			
			System.out.printf("%.3f%%\n", ratio);
		}
		
	}
}