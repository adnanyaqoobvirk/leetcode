class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        while num > 0:
            if num >= 1000:
                cnt, num = divmod(num, 1000)
                ans.append("M" * cnt)
            elif num >= 900:
                num %= 900
                ans.append("CM")
            elif num >= 500:
                num %= 500
                ans.append("D")
            elif num >= 400:
                num %= 400
                ans.append("CD")
            elif num >= 100:
                cnt, num = divmod(num, 100)
                ans.append("C" * cnt)
            elif num >= 90:
                num %= 90
                ans.append("XC")
            elif num >= 50:
                num %= 50
                ans.append("L")
            elif num >= 40:
                num %= 40
                ans.append("XL")
            elif num >= 10:
                cnt, num = divmod(num, 10)
                ans.append("X" * cnt)
            elif num >= 9:
                num %= 9
                ans.append("IX")
            elif num >= 5:
                num %= 5
                ans.append("V")
            elif num >= 4:
                num %= 4
                ans.append("IV")
            else:
                ans.append("I" * num)
                break
        return "".join(ans)