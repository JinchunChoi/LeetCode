'''
Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

# I try to use BFS to handle this problem, but it is not working well.
# I change to use DP (Dynamic Programming) way.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
          
        for i in range(1, rows):
            grid[i][0] += grid[i-1][0] # cumulate first row
        for j in range(1, cols):
            grid[0][j] += grid[0][j-1] # cumulate first column
            
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]) # set a minimum value between from left and above
        return grid[-1][-1] 
        
            
#         q = collections.deque()
#         q.appendleft((0,0,0))              
#         while q:            
#             i, j, val = q.pop()            
#             if i < rows and j < cols:
#                 # update minimum value                                
#                 tmp[i][j] = min(tmp[i][j], (val + grid[i][j]))
                
#                 q.appendleft((i+1, j, tmp[i][j]))
#                 q.appendleft((i, j+1, tmp[i][j]))
#             print i, j, val
#             print tmp
#         print tmp
        
