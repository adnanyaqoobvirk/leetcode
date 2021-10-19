class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = defaultdict(lambda: -1)
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                nextGreater[stack.pop()] = num
            stack.append(num)
        
        ans = []
        for num in nums1:
            ans.append(nextGreater[num])
        return ans