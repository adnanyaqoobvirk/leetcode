class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        j = p = cnt = 0
        for i in range(n + 1):
            if i == n or chars[p] != chars[i]:
                chars[j] = chars[p]
                j += 1
                k = 0
                if cnt > 1:
                    while cnt >= 1:
                        cnt, d = divmod(cnt, 10)
                        chars[j + k] = str(d)
                        k += 1

                    l, r = j, j + k - 1
                    while l < r:
                        chars[l], chars[r] = chars[r], chars[l]
                        l += 1
                        r -= 1
                j += k
                p = i
                cnt = 1
            else:
                cnt += 1
        return j