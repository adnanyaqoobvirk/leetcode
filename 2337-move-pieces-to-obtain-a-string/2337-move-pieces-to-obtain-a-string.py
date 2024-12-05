class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        j = 0
        for i in range(n):
            if target[i] == "L":
                for k in range(j, n):
                    if start[k] == "R":
                        return False

                    if start[k] == "L" and k >= i:
                        j = k + 1
                        break
                else:
                    return False
            elif target[i] == "R":
                for k in range(j, n):
                    if start[k] == "L":
                        return False

                    if start[k] == "R" and k <= i:
                        j = k + 1
                        break
                else:
                    return False
        return True