class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ng_map = defaultdict(lambda: -1)
        stack = []
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            ng_map[num] = -1 if not stack else stack[-1]
            stack.append(num)
        return [ng_map[num] for num in nums1]