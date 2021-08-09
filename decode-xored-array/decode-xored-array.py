class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        output = [first]
        for num in encoded:
            output.append(output[-1] ^ num)
        return output