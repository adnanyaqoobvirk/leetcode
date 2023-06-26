class Solution:
    def countElements(self, arr: List[int]) -> int:
        heapify(arr)
        prev, count, duplicates = heappop(arr), 0, 1
        while arr:
            curr = heappop(arr)
            if curr == prev:
                duplicates += 1
            else:
                if curr == prev + 1:
                    count += duplicates
                duplicates = 1
            prev = curr
        return count