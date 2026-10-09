class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Input: fruits = [1,2,1,3]
        # Output: 3
        count = defaultdict(int) # fruittype -> countFruit
        l = 0
        total = 0
        res = 0

        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1

            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                total -= 1
                l += 1

                if not count[f]:
                    count.pop(f)

            res = max(res, total)
        return res

