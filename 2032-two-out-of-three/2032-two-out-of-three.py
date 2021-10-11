class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        freq = {}
        ans = []
        for nums in [nums1, nums2, nums3]:
            nums = set(nums)
            for num in nums:
                count = freq.get(num, 0)
                if count == 1:
                    ans.append(num)
                    freq[num] = float('-inf')
                else:
                    freq[num] = count + 1
        return ans