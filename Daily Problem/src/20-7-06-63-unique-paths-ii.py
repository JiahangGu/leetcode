#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/6 9:28
# @Author:JiahangGu
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        :设当前格子为ob[i][j]，如果没有障碍物，到达该格子的路径个数为ob[i-1][j]的路径数加ob[i][j-1]的路径书
        定义状态dp[i][j]为到达格子ob[i][j]的路径数，则
        初始化条件：最上边和最左边的格子如果有障碍物则为0，否则等于前一个格子，因为边界只有一条路可以走
        最终结果：dp[m][n]即右下角
        状态转移方程：dp[i][j] = dp[i-1][j] + dp[i][j-1] if ob[i][j] == 1 else 0
        :param obstacleGrid:
        :return:
        '''
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        for i in range(1, n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i-1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]


s = Solution()
test = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print(s.uniquePathsWithObstacles(test))