package DSA;

public class TrappinRainWater {
	
	public int trap(int[] height) {
        
        int [] left = new int[height.length];
        int [] right = new int[height.length];
        int maxLeft = Integer.MIN_VALUE;
        int maxRight = Integer.MIN_VALUE;
        int water = 0;
        for(int i = 0; i < height.length; i++){
            maxLeft  = Math.max(maxLeft, height[i]);
            left[i] = maxLeft;
        }
        
        for(int i = height.length - 1; i >= 0; i--){
            maxRight = Math.max(maxRight, height[i]);
            right[i] = maxRight;
        }
        
        for(int i = 0; i < height.length; i++){
            water += Math.max(Math.min(left[i], right[i]) - height[i], 0);
        }
        return water;
	}

}
