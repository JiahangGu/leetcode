#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/20 15:34
# @Author:JiahangGu
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        正方形的面积由边长决定，所以需要求解最大边长。而边长由该点本身和其余点决定，假设以右下角为基准，
        如果当前点是1，则上点、左点、左上点都是1时才会得到更大的正方形，即由上述点的最小的点决定。
        假设dp[i][j]为以i,j为右下角的最大正方形边长，则dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        注意到边界的点只能是0或1。最终结果是统计所有点为右下角得到的最大边。返回平方为面积
        :param matrix:
        :return:
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            dp[0][i] = int(matrix[0][i])
        for j in range(m):
            dp[j][0] = int(matrix[j][0])
        ans = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0
        return ans * ans


s = Solution()
m = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(s.maximalSquare(m))
