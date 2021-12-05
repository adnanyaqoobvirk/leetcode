class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        def get_digits(n: int) -> List[int]:
            counts = [0] * 10
            n = num
            while n > 0:
                n, r = divmod(n, 10)
                counts[r] += 1
            return counts
                
        counts = Counter(digits)
        ans = []
        for num in range(100, 1000):
            if num % 2 == 0:
                dcounts = get_digits(num)
                for d in range(10):
                    if counts[d] < dcounts[d]:
                        break
                else:
                    ans.append(num)
        return ans