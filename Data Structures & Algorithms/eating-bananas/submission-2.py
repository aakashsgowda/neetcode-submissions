class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Input: piles = [1,4,3,2], h = 9

        # Output: 2
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) //2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res



        