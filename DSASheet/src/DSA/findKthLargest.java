package DSA;

import java.util.Arrays;
import java.util.PriorityQueue;

public class findKthLargest {
	
public int findKthLargest(int[] nums, int k) {
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        Arrays.sort(nums);
        
        for(int i : nums){
            pq.add(i);
            
            if(pq.size() > k){
                pq.remove();
            }
        }
        
        return pq.peek();
    }

}
