class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(lo: int, hi: int, i: int) -> int:
            nums[i], nums[hi] = nums[hi], nums[i]
            
            k = lo
            for j in range(lo, hi):
                if nums[j] < nums[hi]:
                    nums[j], nums[k] = nums[k], nums[j]
                    k += 1
            nums[k], nums[hi] = nums[hi], nums[k]
            return k
        
        def select(left: int, right: int, ns: int) -> int:
            if left == right:
                return nums[left]
            
            idx = partition(left, right, randint(left, right))
            if idx == ns:
                return nums[idx]
            elif idx > ns:
                return select(left, idx - 1, ns)
            else:
                return select(idx + 1, right, ns)
        return select(0, len(nums) - 1, len(nums) - k)