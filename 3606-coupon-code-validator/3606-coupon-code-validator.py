class Solution:
    VALID_CHARS = frozenset(ascii_letters + digits + "_")
    VALID_CATEGORIES = frozenset([
        "electronics",
        "grocery",
        "pharmacy",
        "restaurant"
        ]
    )

    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def isCodeValid(codeString: str) -> bool:
            if not codeString:
                return False

            for ch in codeString:
                if ch not in self.VALID_CHARS:
                    return False
            
            return True

        n = len(code)
        valid_codes = []
        
        for i in range(n):
            if not isActive[i]:
                continue
            
            if not isCodeValid(code[i]):
                continue
            
            if businessLine[i] not in self.VALID_CATEGORIES:
                continue
            
            valid_codes.append((businessLine[i], code[i]))
        
        valid_codes.sort()

        return [codeString for _, codeString in valid_codes]