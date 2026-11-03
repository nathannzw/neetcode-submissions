class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles[i] is number of bananas in ith pile
        # h is number of hours to eat all bananas
        # k is bananas-per-hour eating rate
        # return min(k) to eat within h

        # intuition:
        # h >= len(piles) because max one pile in one hour (each time)
        # k upper bound is max(piles) such that it can take every pile in an hour
        # k lower bound is 1 (based on all pile size is 1 scenario)
        # perform binary search over 1 to max(piles) for the correct k

        l, r = 1, max(piles)

        while l <= r:
            k = (l + r) // 2 # current simulation k (speed)
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / k)
            if total_time <= h:
                res = k # record valid speed, try to find even slower one
                r = k - 1
            else:
                l = k + 1
            
        return res
