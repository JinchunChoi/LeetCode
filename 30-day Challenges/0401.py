# up: 4092, down: 152
# 136. Single Number

# T: O(n), S: O(n)
# I use hashmap and search a single number

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        for k, v in count.items():
            if v == 1:
                return k
            
        
