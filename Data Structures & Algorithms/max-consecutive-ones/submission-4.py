class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Iteration 1
        res = cnt = 0
        for num in nums:
            if num == 0:
                res = max(res, cnt)
                cnt = 0
            else:
                cnt += 1
        return max(res, cnt)
        