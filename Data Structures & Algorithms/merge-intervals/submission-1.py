class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Input: intervals = [[1,3],[1,5],[6,7]]
        # Output: [[1,5],[6,7]]
        
        intervals.sort(key = lambda interval:interval[0])

        merged = []

        for current in intervals:
            current_start = current[0]
            current_end = current[1]

            if not merged:
                merged.append(current)
                continue

            last = merged[-1]
            last_end = last[1]

            if current_start <= last_end:
                last[1] = max(last_end,current_end)
            else:
                merged.append(current)
        return merged
                
            
        