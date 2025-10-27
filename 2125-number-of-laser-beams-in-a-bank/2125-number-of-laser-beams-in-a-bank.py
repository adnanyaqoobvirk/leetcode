class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev_bcount = 0
        for floor in bank:
            curr_bcount = Counter(floor)["1"]

            if curr_bcount == 0:
                continue
            
            ans += prev_bcount * curr_bcount
            prev_bcount = curr_bcount
        return ans