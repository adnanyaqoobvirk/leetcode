class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mor = [0] * (n + 1)
        for i in reversed(range(n)):
            mor[i] = mor[i + 1] | nums[i]
        
        m = mor[0].bit_length()
        minLenPerBit = [[0] * n for _ in range(m)]
        for i in range(m):
            stack = []
            for r in range(n):
                stack.append(r)
                if nums[r] & (1 << i):
                    while stack:
                        l = stack.pop()
                        minLenPerBit[i][l] = r - l + 1
        
        ans = []
        for i in range(n):
            imaxLen = 1
            for j in range(m):
                if mor[i] & (1 << j):
                    imaxLen = max(imaxLen, minLenPerBit[j][i])
            ans.append(imaxLen)
        return ans