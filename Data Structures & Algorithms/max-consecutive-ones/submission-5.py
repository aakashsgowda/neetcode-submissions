class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Iteration 2
        res, cnt = 0, 0
        for num in nums:
            # cnt = cnt + 1 if num else 0
            if num:
                cnt += 1
            else:
                cnt = 0
            res = max(res, cnt)
        return res
        