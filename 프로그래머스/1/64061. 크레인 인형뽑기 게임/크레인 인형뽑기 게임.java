import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0; // 터트린 인형의 수
        Stack<Integer> basket = new Stack<Integer>(); // 뽑은 인형 저장
        
        for(int col : moves){
            col -= 1;
            
            for(int row = 0; row < board.length; row++){
                if(board[row][col] != 0){ //해당 칸에 인형이 있으면
                    if(basket.empty())
                        basket.push(board[row][col]);
                    else{
                        if(board[row][col] == basket.peek()){
                            basket.pop();
                            answer += 2;
                        }else
                            basket.push(board[row][col]);
                    }
                    board[row][col] = 0;
                    break;
                }
            }
        }
        
        return answer;
    }
}