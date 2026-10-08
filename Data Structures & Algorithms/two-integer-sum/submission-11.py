class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #   nums = [3,4,5,6]
        #   target = 7
        #   [0,1]  
        
        #   First Iter: 0, 3
        #   prevMap ={}
        #   dif = 7 - 3 = 4
        #   not in prevMap
        #   prevMap = {0:3}

        #   second iter : 1,4
        #   prevMap = {0:3}
        #   dif = 7 -4 = 3
        #   3 in prevMap
        #   so return 0, 1


        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i ]
            prevMap[n] = i

        