class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        total_ors = set()
        curr_ors = set()
        for num in arr:
            next_ors = {num}
            total_ors.add(num)
            for v in curr_ors:
                next_ors.add(num | v)
                total_ors.add(num | v)
            curr_ors = next_ors
        return len(total_ors)