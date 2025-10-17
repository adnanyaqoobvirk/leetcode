class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def dp(i: int, changed: bool, mask: int) -> int:
            if i >= n:
                return 0
            
            nmask = mask | char_masks[s[i]]
            if nmask.bit_count() > k:
                ans = 1 + dp(i + 1, changed, char_masks[s[i]])
            else:
                ans = dp(i + 1, changed, nmask)

            if not changed:
                for c in ascii_lowercase:
                    cmask = mask | char_masks[c]
                    if cmask.bit_count() > k:
                        ans = max(ans, 1 + dp(i + 1, True, char_masks[c]))
                    else:
                        ans = max(ans, dp(i + 1, True, cmask))
            return ans

        n = len(s)
        char_masks = {c : 1 << ord(c) - ord('a') for c in ascii_lowercase}
        return dp(0, False, 0) + 1