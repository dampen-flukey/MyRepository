package DSA;

public class Kadane {
	public static void main(String[] args) {
		int[] nums = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
		int max = maxSubArray(nums);
		System.out.println(max);

	}

	public static int maxSubArray(int[] nums) {
		int start = 0;
		int end = nums.length;
		int max = Integer.MIN_VALUE;
		int currentSum = 0;
		for (int i = start; i < end; i++) {
			currentSum = currentSum + nums[i];
			if (currentSum > max) {
				max = currentSum;

			}
			if (currentSum < 0) {
				currentSum = 0;
			}

		}

		return max;
	}
}
