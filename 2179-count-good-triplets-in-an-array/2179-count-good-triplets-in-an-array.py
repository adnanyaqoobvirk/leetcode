class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def update(i: int) -> None:
            while i < n:
                bit[i] += 1
                i += i & -i

        def query(i: int) -> int:
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res
        
        num1_indexes = {v: i for i, v in enumerate(nums1)}
        indexes = [num1_indexes[nums2[i]] for i in range(len(nums2))]
        n = len(indexes) + 1
        bit = [0] * n

        count = 0
        for i, idx in enumerate(indexes):
            smaller = query(idx + 1)
            greater = n - 2 - idx - i + smaller
            count += smaller * greater
            update(idx + 1)
        return count