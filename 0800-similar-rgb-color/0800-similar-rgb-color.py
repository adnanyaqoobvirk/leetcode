class Solution:
    def similarRGB(self, color: str) -> str:
        HEX_CHARS = "0123456789abcdef"
        ans = ['#']
        for i in range(1, len(color), 2):
            if color[i] == color[i + 1]:
                ans.append(f"{color[i]}{color[i]}")
            else:
                h = int(f"{color[i]}{color[i + 1]}", 16)
                min_diff = inf
                min_diff_c = ""
                for c in HEX_CHARS:
                    diff = abs(int(f"{c}{c}", 16) - h)
                    if diff < min_diff:
                        min_diff_c = c
                        min_diff = diff
                ans.append(f"{min_diff_c}{min_diff_c}")
        return "".join(ans)