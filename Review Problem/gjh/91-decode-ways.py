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
        注意0不能作为单独的数字出现并且也不能作为两位数的十位数出现。并且如果出现0之前的数字大于2就没有符合条件的解。
        :param s:
        :return:
        """
        # n = len(s)
        # if s[0] == '0':
        #     return 0
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # if n == 2:
        #     if s[1] == '0' and s >= '30':
        #         return 0
        # dp = [0] * n
        # if s[n - 1] == '0':
        #     if s[n - 2] > '2':
        #         return 0
        # if s[n - 1] != '0':
        #     dp[n - 1] = 1
        # dp[n - 2] = 1 + (dp[n - 1] if '10' <= s[-2:] <= '26' else 0)
        # if s[n - 2] == '0':
        #     dp[n - 2] = 0
        # for i in range(n - 3, -1, -1):
        #     if s[i] == '0':
        #         if i == 0 or s[i - 1] >= '3':
        #             return 0
        #         dp[i] = 0
        #     else:
        #         dp[i] = dp[i + 1] + (dp[i + 2] if '10' <= s[i:i + 2] <= '26' else 0)
        # return dp[0]
        """
        上述题解通过了样例，但是代码逻辑太乱，特殊情况的判断应该可以加入到循环中。在此写一个简洁版本的动态规划。
        """
        # if s[0] == '0':
        #     return 0
        # n = len(s)
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(1, n):
        #     if s[i] == '0':
        #         if s[i - 1] == '2' or s[i - 1] == '1':
        #             dp[i + 1] = dp[i - 1]
        #         else:
        #             return 0
        #     elif s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
        #         dp[i + 1] = dp[i] + dp[i - 1]
        #     else:
        #         dp[i + 1] = dp[i]
        # return dp[n]
        """
        观察上述方法发现求当前dp[i]时只需要利用前两个状态，所以可以使用两个变量将空间复杂度从O(n)降低到O(1)。
        cur表示dp[i], pre表示dp[i-1]。每此更新时，cur对应更新为dp[i+1]，pre更新为dp[i]
        """
        if s[0] == '0':
            return 0
        n = len(s)
        cur, pre = 1, 1
        for i in range(1, n):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    x = cur
                    cur = pre
                    pre = x
                else:
                    return 0
            elif s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                x = pre
                pre = cur
                cur = x + cur
            else:
                pre = cur
        return cur


s = Solution()
print(s.numDecodings('227'))
