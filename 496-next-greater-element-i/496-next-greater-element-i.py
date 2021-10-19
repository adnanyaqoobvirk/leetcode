class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        positions = {nums2[i]:i for i in range(len(nums2))}
        ans = []
        for num1 in nums1:
            nxt = -1
            for i in range(positions[num1] + 1, len(nums2)):
                if nums2[i] > num1:
                    nxt = nums2[i]
                    break
            ans.append(nxt)
        return ans