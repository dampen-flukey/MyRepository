package DSA;

import java.util.HashMap;
import java.util.Map;

public class SearchinRotatedSortedArray {
	
	public int search(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
        }
        
        if(!map.containsKey(target))
            return -1;
        else
            return map.get(target);
    }

}
