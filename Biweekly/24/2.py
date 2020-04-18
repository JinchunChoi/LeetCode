# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

# Solution, Greedy
# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/discuss/585836/Python-Greedy
# Building a precomputed list of fibonacci takes O(N). Having 50 fibonacci is going to be sufficiently larger than 
# the limit of k ( 1 <= k <= 10^9). Then, greedily find the largest number which is smaller than k, and subtract 
# the number from k until k becomes 0.

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
