#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/4 16:52
# @Author:JiahangGu

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        动态规划。
        dp[i][j] = dp[i-1][j] + dp[i][j-1]。
        注意对边缘的所有位置都要初始化为1.因为只能有一种方案。
        :param m:
        :param n:
        :return:
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]