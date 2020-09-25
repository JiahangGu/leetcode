#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/24 22:04
# @Author:JiahangGu
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        记忆化搜索可做，当前字符所能得到的解码方案数为x(s[1:])+(x(s[2:]) if '10' <= s[:2] <= '26 else 0)
        然后进一步可以使用动态规划的思想，假设dp[i]表示以s[i]开始的字符串可以得到的解码方案，则
        状态转移可以写成dp[i] = dp[i-1] + (dp[i-2] if 后两位大于10小于26)
        初始化dp[n-1]=1,dp[n-2] = 2 if s[-2:]属于[10,26] else 1
        最终解为dp[0]
        注意0不能作为单独的数字出现并且也不能作为两位数的十位数出现。
        :param s:
        :return:
        """
        n = len(s)
        if s[0] == '0':
            return 0
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * n
        if s[n - 1] != '0':
            dp[n - 1] = 1
        dp[n - 2] = 1 + dp[n - 1] if '10' <= s[-2:] <= '26' else 0
        if s[n - 2] == '0':
            dp[n - 2] = 0
        for i in range(n - 3, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1] + (dp[i + 2] if '10' <= s[i:i+2] <= '26' else 0)
        return dp[0]


s = Solution()
print(s.numDecodings('10'))