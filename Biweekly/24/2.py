'''
1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
Given the number k, return the minimum number of Fibonacci numbers whose sum is equal to k, whether a Fibonacci number could be used multiple times.

The Fibonacci numbers are defined as:

F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 , for n > 2.
It is guaranteed that for the given constraints we can always find such fibonacci numbers that sum k.
 

Example 1:

Input: k = 7
Output: 2 
Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
For k = 7 we can use 2 + 5 = 7.
Example 2:

Input: k = 10
Output: 2 
Explanation: For k = 10 we can use 2 + 8 = 10.
Example 3:

Input: k = 19
Output: 3 
Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
 

Constraints:

1 <= k <= 10^9
'''

# Solution, Greedy
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def fibo(num):
            if num in memo: return memo[num]
            memo[num] = fibo(num - 1) + fibo(num - 2)
            return memo[num]
            
        memo = {1: 1, 2: 1}
        cur_fibo = 50
        fibo(cur_fibo) # precompute
        cnt = 0

        while k > 0:
            for f in range(cur_fibo, 1, -1):
                if memo[f] <= k:
                    k -= memo[f]
                    cur_fibo = f
                    cnt += 1
                    break
        return cnt


# I tried DP to pre-compute fib number less than K, but it meets Memory Limit Exceeded
'''
def fib(n):
        # dp = []
        # dp.append(1)
        # dp.append(1)

        dp = [0] * 3
        dp[0] = 1
        dp[1] = 1

        for i in range(2, k):
        #     if dp[i-2] + dp[i-1] > k:
        #         break        
        #     dp.append(dp[i-2] + dp[i-1])
        # return dp[-1]

            if dp[1] + dp[0] > k:
                    break

            dp[2] = dp[1] + dp[0]
            dp[0] = dp[1]
            dp[1] = dp[2]



        return dp[2]

    print fib(k)

    count = 0
        
#         for d in dp[::-1]:
#             # print d, k
#             if k >= d:
#                 k -= d
#                 count += 1
#             if k == 0:
#                 return count
        
#         if k in dp:
#             return 1
'''
