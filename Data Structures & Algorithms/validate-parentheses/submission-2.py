class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis_map = {"(": ")", "[": "]", "{": "}"}

        for c in s:
            if c in parenthesis_map:
                stack.append(c)
            else:
                if stack and parenthesis_map[stack[-1]]==c:
                    stack.pop()
                else:
                    return False
        
        if len(stack) > 0:
            return False
        return True
