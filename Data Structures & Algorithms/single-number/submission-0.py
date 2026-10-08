class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        duplicate = set()

        for num in nums:
            if num in duplicate:
                duplicate.remove(num)
            else:
                duplicate.add(num)
        
        return list(duplicate)[0]
        