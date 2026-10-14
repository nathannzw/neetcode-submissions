class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointer solution
        l, r = 0, 1
        max_profit = 0

        for i in range (1, len(prices)):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r]-prices[l])
            else:
                l = r
                
            r += 1

        return max_profit