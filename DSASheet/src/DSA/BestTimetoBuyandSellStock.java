package DSA;

import java.util.HashMap;
import java.util.Map;

public class BestTimetoBuyandSellStock {
	
public int maxProfit(int[] prices) {
       
        
        Map<Integer, Integer> map = new HashMap();
        
        
        int buy = 0;
        //int sellAmt = Integer.MAX_VALUE;
        int sell = buy+1;
        int max = 0;
        int diff = 0;
        while(sell < prices.length){
            if(prices[sell] > prices[buy]){
                diff = prices[sell] - prices[buy];
                if(diff > max){
                    max = diff;
                }
            }else{
                buy = sell;
            }
            sell++;
        }
        return max;
    }

}
