#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/4 16:55
# @Author:JiahangGu
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        动态规划，dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]。
        注意应初始化边界为路径和。
        :param grid:
        :return:
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[None for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        for i in range(1, n):
            dp[0][i] = grid[0][i] + dp[0][i - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]
