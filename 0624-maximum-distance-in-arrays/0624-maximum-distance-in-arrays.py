class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        first = second = (inf, 0)
        third = fourth = (-inf, 0)
        for i, arr in enumerate(arrays):
            f, l = arr[0], arr[-1]
            
            if f < first[0]:
                second, first = first, (f, i)
            elif f < second[0]:
                second = (f, i)
            
            if l > fourth[0]:
                third, fourth = fourth, (l, i)
            elif l > third[0]:
                third = (l, i)
        
        if first[1] == fourth[1]:
            return max(abs(second[0] - fourth[0]), abs(first[0] - third[0]))
        else:
            return abs(first[0] - fourth[0])