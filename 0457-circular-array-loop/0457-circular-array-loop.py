class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def invalid(ptr: int) -> int:
            if (nums[ptr] < 0) != neg or nums[ptr] % n == 0:
                return True
            else:
                return False
        n = len(nums)
        for i in range(n):
            neg = nums[i] < 0
            slow = fast = i
            while True:
                slow = (slow + nums[slow]) % n
                if invalid(slow):
                    break
                
                fast = (fast + nums[fast]) % n
                if invalid(fast):
                    break

                fast = (fast + nums[fast]) % n
                if invalid(fast):
                    break

                if slow == fast:
                    return True
        return False