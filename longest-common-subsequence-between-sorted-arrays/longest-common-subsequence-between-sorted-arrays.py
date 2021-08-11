class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        n = len(arrays)
        
        num_count = {}
        for array in arrays:
            for num in array:
                num_count[num] = num_count.get(num, 0) + 1
                
        return [num for num, count in num_count.items() if count == n]