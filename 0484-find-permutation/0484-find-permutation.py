class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ans = []
        start = 1
        count = 1
        for c in s:
            if c == "I":
                for num in reversed(range(start, start + count)):
                    ans.append(num)
                start = start + count
                count = 1
            else:
                count += 1
        for num in reversed(range(start, start + count)):
            ans.append(num)
        return ans