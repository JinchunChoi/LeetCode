# up: 4550, down: 207

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Use stack, T: O(n), S: O(n)
        stack = []
        
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')' or c == '}' or c == ']':
                if stack:
                    tmp = stack.pop()
                else:
                    tmp = ''
                if (c == ')' and tmp != '(') or (c == '}' and tmp != '{') or (c == ']' and tmp != '['):
                    return False
                
        return True if len(stack) == 0 else False
