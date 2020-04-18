# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

# use recursive and sorting


class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Solution
        res=[]     # list storing all the strings of size n  
        def fun(s, curr, n):  # recurisve function for finding all strings
            if n==0 :                  
                res.append(curr)
                return
            for i in range(3):  #checking whether the currently buildup string's last charachter matches to the new charachter we are appending
                if curr and curr[-1]==s[i]:   
                    continue
                modify_curr=curr+s[i]       # modify current string       
                fun(s, modify_curr, n-1)  
        fun(['a','b','c'],"",n)
        res=sorted(res)      #lexicographically sorted
        return res[k-1] if k <= len(res) else ""    
        
        # Failed to solve
#         char = ['a','b','c']
        
#         def helper(n, path):
#             if n == 0:
#                 return path
#             if path[-1] != 
