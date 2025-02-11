class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= len(part):
                i = -1
                for p in reversed(part):
                    if p != stack[i]:
                        break
                    i -= 1
                else:
                    while i < -1:
                        stack.pop()
                        i += 1
        return "".join(stack)
