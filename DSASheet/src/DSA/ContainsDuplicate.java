package DSA;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class ContainsDuplicate {
	public boolean containsDuplicate(int[] nums) {
		boolean flag = false;
		Map<Integer, Integer> map = new HashMap<>();
		for (int i = 0; i < nums.length; i++) {
			if (!map.containsKey(nums[i])) {
				map.put(nums[i], 1);
			} else {
				map.put(nums[i], map.get(nums[i]) + 1);
			}
		}
		Set<Integer> set = map.keySet();

		for (int i : set) {
			if (map.get(i) > 1) {
				flag = true;
			}
		}
		return flag;

	}
	

    public boolean containsDuplicateUsingSet(int[] nums) {
        
        boolean flag = false;
        
        Set<Integer> set = new HashSet<>();
        
        for(int i = 0; i < nums.length; i++){
            if(!set.add(nums[i])){
                flag = true;
                
            }
        }
        return flag;
    }
}
