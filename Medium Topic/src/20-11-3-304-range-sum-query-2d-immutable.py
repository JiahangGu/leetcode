#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/11/3 17:26
# @Author:JiahangGu
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        设dp[i][j]表示[0,0]到[i,j]的元素和，则要求元素总和时dp[r2][c2]-dp[r2][c1]-dp[r1][c2]+dp[r1][c1]
        :param matrix:
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        self.dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.dp[i][j] = self.dp[i - 1][j] + self.dp[i][j - 1] - self.dp[i - 1][j - 1] + matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
