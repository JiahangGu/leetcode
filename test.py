#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/29 10:03
# @Author:JiahangGu
from typing import List


class Solution:
    # def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
    #     from collections import defaultdict
    #     cnt = defaultdict(int)
    #     for item in requests:
    #         for i in range(item[0], item[1]+1):
    #             cnt[i] += 1
    #     nums.sort(reverse=True)
    #     result = sorted(cnt.items(), key=lambda d:d[1], reverse = True)
    #     i = 0
    #     ans = 0
    #     for k, v in result:
    #         ans = (ans + v * nums[i]) % (10**9+7)
    #         i += 1
    #     return ans
    # def minSubarray(self, nums: List[int], p: int) -> int:
    #     res = sum(nums) % p
    #     if res == 0:
    #         return 0
    #     if sum(nums) < p:
    #         return -1
    #     l, r = 0, 0
    #     ans = 1e9
    #     cur_sum = 0
    #     while l <= r and l < len(nums) and r < len(nums):
    #         cur_sum += nums[r]
    #         if cur_sum == res:
    #             ans = min(r-l+1, ans)
    #             cur_sum -= nums[l]
    #             l += 1
    #             cur_sum -= nums[r]
    #         elif cur_sum < res:
    #             r += 1
    #         elif cur_sum > res:
    #             cur_sum -= nums[l]
    #             l += 1
    #             if l > r:
    #                 r += 1
    #             else:
    #                 cur_sum -= nums[r]
    #     return ans if ans < 1e9 else -1
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        dp = [[[0] * n for _ in range(m)] for _ in range(2)]
        dp[0][m-1][n-1] = dp[1][m-1][n-1] = grid[m-1][n-1]
        for i in range(m-2, -1, -1):
            dp[0][i][n-1] = dp[0][i+1][n-1] * grid[i][n-1]
            dp[1][i][n - 1] = dp[1][i + 1][n - 1] * grid[i][n - 1]
        for j in range(n-2, -1, -1):
            dp[0][m-1][j] = dp[0][m-1][j+1] * grid[m-1][j]
            dp[1][m - 1][j] = dp[1][m - 1][j + 1] * grid[m - 1][j]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                right1 = dp[0][i][j+1]
                down1 = dp[0][i+1][j]
                right2 = dp[1][i][j + 1]
                down2 = dp[1][i + 1][j]
                if grid[i][j] < 0:
                    dp[0][i][j] = min(right2, down2) * grid[i][j]
                    dp[1][i][j] = max(right1, down1) * grid[i][j]
                else:
                    dp[0][i][j] = max(right1, down1) * grid[i][j]
                    dp[1][i][j] = min(right2, down2) * grid[i][j]
        res = max(dp[0][0][0], dp[1][0][0])
        if res < 0:
            return -1
        return res % MOD


s = Solution()
# print(s.maxSumRangeQuery([1,2,3,4,5,10], [[0,2],[1,3],[1,1]]))
grid = [[1,-1,0,-3,4,3,-3,3,-1,3,0,0,-4,2],[2,-2,-3,-4,0,-2,-3,3,1,4,1,-3,-1,-4],[-4,4,-4,-4,2,-4,3,0,-2,-4,3,4,-1,0],[-3,3,-4,-4,3,4,4,1,-1,-1,0,3,4,1],[1,3,-4,2,2,-3,1,-3,-4,-4,-1,-4,-4,4],[1,1,-1,1,-1,-1,3,-4,-1,2,-2,3,-4,0],[1,0,3,3,1,4,1,1,-4,-1,-3,4,-4,4],[4,3,2,3,0,-1,2,-4,1,0,0,1,3,4],[-4,4,-4,-4,2,-2,2,-1,0,-2,2,4,-2,-1],[-2,3,4,-4,3,3,-2,-1,0,-3,4,-2,-1,-4],[4,3,3,3,-3,1,2,-4,-1,4,-3,-3,2,0],[3,3,0,1,-4,-4,-3,3,-2,-4,2,4,-3,3],[-3,0,1,3,0,0,0,-4,-1,4,-1,-3,1,1],[-1,4,0,-3,1,-3,-1,2,1,-3,-1,-4,4,1]]
print(s.maxProductPath(grid))
