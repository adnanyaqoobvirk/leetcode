class Solution:
    def isValid(self, s: str) -> bool:
        bmap = {')': '(', '}': '{', ']': '['}
        stack = []
        for b in s:
            if b in bmap:
                if stack and stack[-1] == bmap[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return not stack