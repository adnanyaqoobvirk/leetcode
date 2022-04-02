class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right, invalids = 0, len(s) - 1, 0
        stack = []
        while left < right:
            if s[left] != s[right]:
                if invalids > 0:
                    if not stack:
                        return False
                    else:
                        left, right = stack.pop()
                        continue
                invalids += 1
                if s[left + 1] == s[right]:
                    stack.append((left, right - 1))
                    left += 1
                else:
                    stack.append((left + 1, right))
                    right -= 1
            else:
                left += 1
                right -= 1
        return True