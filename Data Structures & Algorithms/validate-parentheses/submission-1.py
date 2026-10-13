"""
Intuition:
Last opened bracket must be closed first: {([])}
This follows the LAST IN FIRST OUT (LIFO) methodology.
'If see closing bracket, which opening bracket should be at top of stack?'
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for c in s:
            # ensure we don't access opening brackets 
            if c in close_to_open: # ensure we don't access opening brackets 
                # come across a closing bracket
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop() # acknowledge and remove latest opening bracket
                else:
                    return False # logic violation

            else:
                # This case happens first
                stack.append(c) # add all opening brackets to the stack
            
        if not stack:
            return True
        else:
            return False