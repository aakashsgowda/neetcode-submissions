class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Input: cardPoints = [1,2,3,4,5,6,1], k = 3
        # Output: 12

        l, r = 0, len(cardPoints) - k
        total = sum(cardPoints[r:])
        res = total

        while r < len(cardPoints):
            total += (cardPoints[l] - cardPoints[r])
            res = max(total, res)
            l += 1
            r += 1
        return res
        