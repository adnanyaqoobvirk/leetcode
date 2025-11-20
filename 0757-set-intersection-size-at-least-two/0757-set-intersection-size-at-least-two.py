class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        contain_set = []
        for start, end in intervals:
            count = 0
            has_end = False
            for v in reversed(contain_set):
                if v == end:
                    has_end = True
                if start <= v <= end:
                    count += 1
                if count == 2:
                    break
            else:
                if count == 0:
                    contain_set.append(end - 1)
                    contain_set.append(end)
                elif count == 1:
                    if has_end:
                        contain_set.append(end - 1)
                    else:
                        contain_set.append(end)
        return len(contain_set)