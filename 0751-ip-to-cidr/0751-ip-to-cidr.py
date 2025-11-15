class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        def ipToInt(ip: str) -> int:
            res = 0
            for g in ip.split("."):
                res <<= 8
                res += int(g)
            return res
        
        def intToIp(x: int) -> str:
            res = []
            for _ in range(4):
                res.append(str(x & 0xFF))
                x >>= 8
            return ".".join(reversed(res))
        
        def rightZeroCount(x: int) -> int:
            res = 0
            for _ in range(32):
                if x & 1:
                    break
                res += 1
                x >>= 1
            return res
        
        ans = []
        i = ipToInt(ip)
        while n > 0:
            bits = floor(log(n, 2))
            zeros = rightZeroCount(i)

            k = min(bits, zeros)
            prefix = 32 - k

            cidr = f"{intToIp(i)}/{prefix}"
            ans.append(cidr)

            i += 1 << k
            n -= 1 << k
        return ans