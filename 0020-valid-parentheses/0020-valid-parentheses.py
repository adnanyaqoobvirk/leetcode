class Solution:
    def isValid(self, s: str) -> bool:
        def validate(index: int) -> int:
            """
            Parse from index, return the index after valid pair or -1.
            Handles nested and sequential.
            """
            if index >= len(s):
                return index
            
            # Expect opening or end
            if s[index] in ')}]':
                return index  # Return position of closing for parent to match
            
            # Opening: parse inside
            inner_start = index + 1
            inner_end = validate(inner_start)
            if inner_end >= len(s) or not is_match(s[index], s[inner_end]):
                return -1
            
            # After matching pair, continue with next (sequential)
            return validate(inner_end + 1)
        
        # Match helper
        def is_match(open_c: str, close_c: str) -> bool:
            return (open_c == '(' and close_c == ')') or \
                   (open_c == '{' and close_c == '}') or \
                   (open_c == '[' and close_c == ']')
        
        # Whole string must be consumed
        return validate(0) == len(s)