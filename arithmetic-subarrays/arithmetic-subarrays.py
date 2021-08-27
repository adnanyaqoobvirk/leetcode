class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for left, right in zip(l, r):
            # calculate min, max values of subarray             
            mx = mn = None
            for i in range(left, right + 1):
                if mx is None or nums[i] > mx:
                    mx = nums[i]
                if mn is None or nums[i] < mn:
                    mn = nums[i]
            
            # check diff between subarray elements is multiple of pattern           
            size = right - left
            if (mx - mn) % size:
                result.append(False)
            else:
                
                pat = (mx - mn) // size
                if pat == 0:
                    result.append(True)
                else:
                    seen = set()
                    for i in range(left, right + 1):
                        if (nums[i] - mn) % pat or nums[i] in seen:
                            result.append(False)
                            break
                        seen.add(nums[i])
                    else:
                        result.append(True)
        return result