class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index, stack, seen = {c: i for i, c in enumerate(s)}, [], set()
        for i, c in enumerate(s):
            if c not in seen:
                while stack and stack[-1] >= c and i < last_index[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return "".join(stack)