class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        first_six = num.find('6')
        if first_six == -1:
            return num
        else:
            return num[:first_six] + '9' + num[first_six + 1:]