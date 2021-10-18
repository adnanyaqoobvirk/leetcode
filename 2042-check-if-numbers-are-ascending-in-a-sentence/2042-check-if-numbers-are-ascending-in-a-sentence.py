class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        pd = 0
        for ss in s.split(): 
            if ss.isdigit():
                d = int(ss)
                if d <= pd:
                    return False
                pd = d
        return True