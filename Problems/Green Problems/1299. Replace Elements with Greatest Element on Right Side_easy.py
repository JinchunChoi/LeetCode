# up: 251, down: 63

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        for i in range(len(arr)-1, -1, -1):            
            if i == len(arr)-1: # last element
                max_val = arr[i]
                arr[i] = -1
            else:                
                max_prev = max_val
                max_val = max(max_val, arr[i])
                arr[i] = max_prev
        return arr
