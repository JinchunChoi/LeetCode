# up: 14438, down: 526

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Brute force, T: O(n^2), S: O(1)
        for i in range(len(nums)):
            for j in range(i, len(nums)):                
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
        
        
