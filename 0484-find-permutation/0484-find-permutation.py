class Solution:
    def findPermutation(self, s: str) -> List[int]:
        prev, curr, ans = 1, 1, []
        for c in s:
            if c == "I":
                for i in reversed(range(prev, curr + 1)):
                    ans.append(i)
                prev = curr + 1
            curr += 1
        for i in reversed(range(prev, curr + 1)):
            ans.append(i)
        return ans