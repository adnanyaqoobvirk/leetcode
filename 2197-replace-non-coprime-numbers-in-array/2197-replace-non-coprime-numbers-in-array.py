class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a: int, b: int) -> int:
            while b > 0:
                a, b = b, a % b
            return a
        
        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(nums[i])
            while len(ans) > 1:
                num1, num2 = ans.pop(), ans.pop()
                g = gcd(num1, num2)
                if g == 1:
                    ans.append(num2)
                    ans.append(num1)
                    break
                else:
                    ans.append((num1 * num2) // g)
        return ans

            