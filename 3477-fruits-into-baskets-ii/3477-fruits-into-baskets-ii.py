class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        for f in fruits:
            for i in range(len(baskets)):
                if baskets[i] >= f:
                    baskets[i] = -1
                    break
            else:
                count += 1
        return count