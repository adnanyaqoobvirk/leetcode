class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avgs = [-1] * n

        if k >= math.ceil(n / 2):
            return avgs
        
        wsize = 2 * k + 1
        
        wsum = 0
        for i in range(wsize):
            wsum += nums[i]

        avgs[k] = wsum // wsize

        for i in range(wsize, n):
            wsum += nums[i]
            wsum -= nums[i - wsize]

            avgs[i - k] = wsum // wsize
        return avgs
