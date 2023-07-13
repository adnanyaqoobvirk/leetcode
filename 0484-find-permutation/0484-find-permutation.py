class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack, ans, num = [1], [], 1
        for c in s:
            if c == "I":
                while stack:
                    ans.append(stack.pop())
            num += 1
            stack.append(num)
        while stack:
            ans.append(stack.pop())
        return ans