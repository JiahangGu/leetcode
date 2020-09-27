#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/12 9:29
# @Author:JiahangGu
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        假设dp[i]表示第i天结束后的累计最大收益，每天结束后的状态有三种：
        1.目前持有股票，对应dp[i][0]
        2.目前不持有股票，且处于冷冻期,dp[i][1]
        3.目前不持有股票但不在冷冻期，dp[i][2]
        初始化：dp[i][0]=-prices[0]（买入），dp[i][1]=dp[i][2]=0
        解的状态：max(dp[n][1], dp[n][2])对应当天卖出和之前卖出的状态。
        状态转移方程:
        1.dp[i][0]：当天买入一支股票（要求不是冷冻期），或者前一天持有股票,
        dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
        2.dp[i][1]：只能是当天卖出股票（要求前一天持有股票）,dp[i][1]=dp[i-1][0]+prices[i]
        3.dp[i][2]：前一天不持有股票且处于冷冻期，所以当天不买度过冷冻期，或者前一天不持有股票且不处于冷冻期
        dp[i][2]=max(dp[i-1][1], dp[i-1][2])
        :param prices:
        :return:
        '''
        # n = len(prices)
        # if n <= 1:
        #     return 0
        # dp = [[0] * 3 for _ in range(n)]
        # dp[0][0] = -prices[0]
        # for i in range(1, n):
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
        #     dp[i][1] = dp[i - 1][0] + prices[i]
        #     dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        # return max(dp[n-1][1], dp[n-1][2])
        '''
        复杂度优化，上述dp数组迭代过程只需要使用前一个索引的状态，所以可以使用三个变量代替数组记录。
        '''
        n = len(prices)
        if n <= 1:
            return 0
        dp0 = -prices[0]
        dp1 = 0
        dp2 = 0
        for i in range(1, n):
            max0 = max(dp0, dp2 - prices[i])
            max1 = dp0 + prices[i]
            max2 = max(dp1, dp2)
            dp0 = max0
            dp1 = max1
            dp2 = max2
        return max(dp1, dp2)


s = Solution()
x = [1,2,3,0,2]
print(s.maxProfit(x))
