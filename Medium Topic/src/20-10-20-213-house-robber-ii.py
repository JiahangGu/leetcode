#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/20 13:09
# @Author:JiahangGu
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        设dp[i]表示偷到第i个房间时可以得到的最大金额，则状态转移过程需要考虑前一个房间是否被偷过。
        所以需要两个状态：1是记录当前房间偷了的金额，2是当前房间没被偷的金额。
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + nums[i])。
        需要注意，由于形成一个圈，第一个房间和最后一个房间不能同时偷，所以问题拆分为寻找[1:n]和[0:n-1]两个
        子问题中的最大值。
        注意到每个状态求解只需要用到前一个状态的两个值，所以可以将空间复杂度由O(n)减为O(1)。
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        money_stole_1 = nums[0]
        money_nostole_1 = 0
        for i in range(1, n - 1):
            tmp = money_stole_1
            money_stole_1 = max(money_stole_1, money_nostole_1 + nums[i])
            money_nostole_1 = max(money_nostole_1, tmp)
        money_stole_2 = nums[0]
        money_nostole_2 = 0
        for i in range(1, n - 1):
            tmp = money_stole_2
            money_stole_2 = max(money_stole_2, money_nostole_2 + nums[i])
            money_nostole_2 = max(money_nostole_2, tmp)
        return max(money_stole_1, money_stole_2)


s = Solution()
print(s.rob([1,2,3,1]))
