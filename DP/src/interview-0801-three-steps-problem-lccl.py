#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/22 22:06
# @Author:JiahangGu


class Solution:
    def waysToStep(self, n: int) -> int:
        '''
        爬台阶变式，定义状态dp[i]表示到达第i个台阶的方式
        初始化dp[0]=1表示出发点，dp[1]=1, dp[2]=2
        返回结果为dp[n]
        状态转移方程：dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        :param n:
        :return:
        '''
        MAX = 1000000007
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MAX
        return dp[n]
        '''
        类似于斐波那契数列方法，也可以使用快速幂优化，但使用场景少，暂时不补充
        '''


s = Solution()
print(s.waysToStep(5))
