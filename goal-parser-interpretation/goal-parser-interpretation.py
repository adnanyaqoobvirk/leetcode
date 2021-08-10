class Solution:
    def interpret(self, command: str) -> str:
        output = []
        i = 0
        while i < len(command):
            if command[i] == 'G':
                output.append("G")
            elif command[i] == '(':
                if command[i + 1] == ')':
                    output.append('o')
                    i += 1
                else:
                    output.append("al")
                    i += 3
            i += 1
        return "".join(output)