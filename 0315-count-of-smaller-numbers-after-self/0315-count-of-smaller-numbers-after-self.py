class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            if not left:
                return right
            
            if not right:
                return left

            ln, rn = len(left), len(right)
            res = [0] * (ln + rn)
            i, lr, rr = len(res) - 1, ln - 1, rn - 1
            while lr >= 0 or rr >= 0:
                if lr < 0:
                    res[i] = right[rr]
                    rr -= 1
                elif rr < 0:
                    res[i] = left[lr]
                    lr -= 1
                elif nums[left[lr]] > nums[right[rr]]:
                    res[i] = left[lr]
                    ans[left[lr]] += rr + 1
                    lr -= 1
                else:
                    res[i] = right[rr]
                    rr -= 1
                i -= 1
            return res

        def sort(l, r):
            if l > r:
                return []

            if l == r:
                return [indexes[l]]
            
            mid = l + (r - l) // 2
            left = sort(l, mid)
            right = sort(mid + 1, r)

            return merge(left, right)

        n = len(nums)
        indexes = list(range(n))
        ans = [0] * n
        sort(0, n - 1)
        return ans