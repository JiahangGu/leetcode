#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/14 9:37
# @Author:JiahangGu
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        '''
        动态规划算法，如果按照常规思路从左上到右下遍历的方式，会存在如下问题：当前保留的最小值为0，0
        到该点的最小值，但可能由于路径中出现很大正数导致该点得到的值是正数，所以到终点也得到一个正数，
        从而得到不需要初始点数的结论，但在路径的前侧可能存在部分路径需要消耗点数才能到达该点的情况。
        如果考虑从右下到左上的方式，则每个点计算的是到达终点需要具有的最小初始点数，从该点出发保证能
        到达终点。
        定义状态dp[i][j]为从i，j出发到终点的最小初始值，
        状态转移方程：dp[i][j]=max(min(dp[i+1][j], dp[i][j+1]）-dungeon[i][j], 1)，从下面和右面的点走，
        因为要计算最小初始值所以选择小的点，并且因为要消耗点数所以要减去当前点，这样如果是负数就是累加
        计算健康点，并且每一个格子都必须是正数最小为1.
        初始化：要从dp[m-1][n-1]即终点开始，用到dp[m][n-1]和dp[m-1][n]的状态，在这里假设格子存在方便计
        算，则按照定义最小值为1应该初始化为1.其余格子初始值为inf，表示无限生命。
        解状态：dp[0][0]
        :param dungeon:
        :return:
        '''
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[1e12] * (n+1) for _ in range(m+1)]
        dp[m][n-1] = dp[m-1][n] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1])-dungeon[i][j], 1)
        print(dp)
        return dp[0][0]


s = Solution()
x = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(s.calculateMinimumHP(x))
