# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

# I simulated the process.
# During the while loop, if the value i is going less than 1, break loop and return value.



class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0        
        while True:
            i += 1
            tmp = i
            isPass = True
            for n in nums:
                i += n
                if i < 1:
                    isPass = False
                    i = tmp
                    break
            if isPass:
                return tmp
                break

            
