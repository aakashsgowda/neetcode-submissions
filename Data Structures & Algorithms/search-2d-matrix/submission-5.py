class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = [num for row in matrix for num in row]

        # Step 2: Standard binary search on the flat list
        l, r = 0, len(flat) - 1
        while l <= r:
            m = (l + r) // 2
            if flat[m] == target:
                return True
            elif flat[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False





        