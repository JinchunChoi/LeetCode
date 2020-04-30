# up: 576, down: 2240

# Use split function
# T: O(n), S: O(n)
# Python strings are basically immutable, so split function make at least O(n) space.
# https://stackoverflow.com/questions/58503255/space-complexity-of-split-function-in-python

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """        
        return len(s.split()[-1]) if len(s.split()) != 0 else 0
        
