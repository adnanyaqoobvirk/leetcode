class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split('/'):
            if p == '..':
                if stack:
                    stack.pop()
            elif p == '.' or not p:
                continue
            else:
                stack.append(f'/{p}')
        return ''.join(stack) if stack else '/'