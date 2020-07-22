#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/8 22:15
# @Author:JiahangGu

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        定义状态dp[i]为到第i个房屋所能得到的最大金额
        初始化：dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
        结束状态：dp[n-1]
        状态转移方程：dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        :param nums:
        :return:
        '''
        # if len(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        # return dp[len(nums) - 1]
        '''
        空间优化：只需要前两个位置的数字，可以使用两个变量保存。
        '''
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        first = nums[0]
        second = max(first, nums[1])
        for i in range(2, len(nums)):
            tmp = max(first + nums[i], second)
            first = second
            second = tmp
        return second


s = Solution()
x = [1,2,3,1]
print(s.rob(x))