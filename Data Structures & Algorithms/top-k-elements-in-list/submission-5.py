class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # num : count
        # nums=[1, 1, 1, 2, 2, 3]
        # count(freq)     | [0] [1] [2] [3] [4] [5] [6] 
        # numbers(values) |      3   2   1
        
        freq = [[] for i in range(len(nums)+ 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
     


        