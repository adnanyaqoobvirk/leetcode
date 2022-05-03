class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ans, stack, i = [], [1], 1
        for c in s:
            i += 1
            if c == 'D':
                stack.append(i)
            else:
                ans.extend(reversed(stack))
                stack = [i]
        ans.extend(reversed(stack))
        return ans
                