class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        psums = [0]
        for num in nums:
            psums.append(psums[-1] + num)

        avgs = [-1] * n
        wsize = 2 * k + 1
        for i in range(k, n - k):
            avgs[i] = (psums[i + k + 1] - psums[i - k]) // wsize

        return avgs
