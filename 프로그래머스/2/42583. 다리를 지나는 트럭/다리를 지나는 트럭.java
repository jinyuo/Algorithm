import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Truck> qu = new LinkedList<Truck>();
        
        for(int i = 0; i < truck_weights.length;){
            if(weight - truck_weights[i] >= 0){
                qu.add(new Truck(truck_weights[i], answer + bridge_length));
                weight -= truck_weights[i];
                answer++;
                i++;
                //System.out.println(qu);
            }else{
                Truck t = qu.poll();
                answer = answer > t.end_time ? answer : t.end_time;
                weight += t.weight;
            }
            
        }
        // System.out.println(qu);
        
        while(qu.size() != 0)
             answer = qu.poll().end_time;
        
        return answer + 1;
    }
}

class Truck{
    int weight;
    int end_time;
    
    Truck(){
    }
    Truck(int weight, int end_time){
        this.weight = weight;
        this.end_time = end_time;
    }
    
    public String toString(){
        return String.format("w : %d t : %d", weight, end_time);
    }
    
}