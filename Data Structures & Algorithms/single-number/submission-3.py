class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Bit Manipulation
        res = 0
        for num in nums:
            res = res ^ num
        return res
        
        