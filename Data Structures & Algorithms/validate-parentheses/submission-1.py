class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:  # It's a closing bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # Match found
                else:
                    return False  # Mismatch or empty stack
            else:
                stack.append(c)  # It's an opening bracket
        
        return not stack
