class Solution {
    public int solution(int n) {
		Boolean [] primeList = new Boolean[n+1];

		// 2~ n 까지 소수로 설정
		for(int i=2; i<=n; i++ )
            primeList[i] = true;

		// 2 부터  ~ i*i <= n
		// 각각의 배수들을 지워간다.
		for(int i=2; (i*i)<=n; i++){
            for(int j = i*i; j<=n; j+=i)
                if(primeList[i])
                    primeList[j] = false;
				//i*i 미만은 이미 처리되었으므로 j의 시작값은 i*i로 최적화할 수 있다.
		}
		int cnt = 0;
		for(int i=2; i<=n; i++){
			if(primeList[i] == true){
				cnt++;
			}
		}    
        return cnt;
    }

}

// class Solution { 
//     public int solution(int n) { 
//         int answer = 0; 
//         boolean[] sosu =new boolean [n+1]; 
//         for(int i=2; i<=n ; i++) 
//             sosu[i]=true; //2~n번째수를 true로 초기화 
//         //제곱근 구하기 
//         int root=(int)Math.sqrt(n); 
//         for(int i=2; i<=root; i++){ 
//             //2~루트n까지 검사 
//             if(sosu[i]==true){  //i번째의 수가 소수일 때 
//                 for(int j=i; i*j<=n; j++) 
//                     //그 배수들을 다 false로 초기화(배수는 소수가 아니기 때문) 
//                     sosu[i*j]=false; 
//             } 
//         } 
//         for(int i =2; i<=n; i++) { 
//             if(sosu[i]==true) //소수의 개수 세기 
//                 answer++; 
//         } 
//         return answer; 
//     } 
// }