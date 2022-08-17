package DSA;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class RepetedAndMissing {

	public static void main(String[] args) {
		final int [] arr = {3, 1, 2, 5, 3};
		int [] ans = repeatedNumber(arr);
		for(int a : ans) {
			System.out.println(a);
		}

	}
	
public static int[] repeatedNumber(final int[] A) {
        
        Set<Integer> set = new HashSet<>();
        int repeated = -1;
        int missing = -1;
        for(int i = 0; i < A.length; i++){
            
            if(!set.add(A[i])){
                repeated = A[i];
            }
            set.add(A[i]);
        }
        List<Integer> list = new ArrayList<>(set);
        Collections.sort(list);
        
        for(int i = 1; i < list.size(); i++){
            if(list.get(i-1) + 1 != list.get(i)){
                missing = list.get(i - 1) + 1;
            }
        }
        
        int []ans = {repeated, missing};
        return ans;
        
    }

}
