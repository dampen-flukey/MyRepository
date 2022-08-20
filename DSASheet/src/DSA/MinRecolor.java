package DSA;

public class MinRecolor {
	
	public static void main(String[] args) {
		
		String blocks = "WBWBBBW";
		System.out.println(minimumRecolors(blocks,2));
	}
	
	 public static int minimumRecolors(String blocks, int k) {
	        int start = 0;
	        int end = start + k - 1;
	        int count = 0;
	        int ans = Integer.MAX_VALUE;
	        
	        while(end < blocks.length()){
	            for(int i = start; i <= end; i++){
	                if(blocks.charAt(i) == 'W'){
	                    count++;
	                }
	                
	            }
	            ans = Math.min(count, ans);
	            count = 0;
                start++;
                end++;
	        }
	        return ans;
	    }

}
