class Solution {
    fun rob(nums: IntArray): Int {
        if(nums.size == 1)
            return nums[0]
        
        var ans = 0
        for(   
            (start, m) in listOf(Pair(0, nums.size - 1), Pair(1, nums.size))
        ){
            var prev = 0
            var curr = 0
            for(i in start..m - 1)
                prev = curr.also { curr = maxOf(nums[i] + prev, curr) }
            ans = maxOf(ans, curr)
        }
        return ans
    }
}