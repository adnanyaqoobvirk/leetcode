class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        # Generator for combinations
        def generate() -> Iterator[str]:
            n = len(digits)
            indices = [0] * n
            
            while True:
                # Build current combination
                yield ''.join(phone[digits[i]][indices[i]] for i in range(n))
                
                # Increment like an odometer
                for pos in reversed(range(n)):
                    indices[pos] += 1
                    if indices[pos] < len(phone[digits[pos]]):
                        break
                    indices[pos] = 0
                else:
                    break
        
        return list(generate())