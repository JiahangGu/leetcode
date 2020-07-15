#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/14 22:10
# @Author:JiahangGu
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        自顶向下：定义状态dp[i][j]表示从第一行开始到当前位置的最小路径
        初始化：dp[0][0]=triangle[0][0]
        解状态：max(dp[n-1])
        状态转移方程：dp[i][j]=min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        :param triangle:
        :return:
        '''
        # m = len(triangle)
        # dp = [[1e12] * m for _ in range(m)]
        # dp[0][0] = triangle[0][0]
        # for i in range(1, m):
        #     for j in range(i+1):
        #         if j == 0:
        #             dp[i][j] = dp[i-1][j] + triangle[i][j]
        #         else:
        #             dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        # return min(dp[m-1])
        '''
        空间复杂度优化，O(N)解法，发现上述状态转移方程中只需要用到前一行的状态，
        可以使用一个n维数组，在计算i,j时，前j个仍是上一行的状态，j之后则是第i行的值
        则使用f[j]=min(f[j-1], f[j])+triangle[i][j]转移状态，这样的划分是因为状态转
        移时依赖于上一行的[j]和[j-1]，所以需要逆序枚举，如果采用正序枚举则[j-1]表示
        当前行的状态，不符合定义。
        '''
        m = len(triangle)
        dp = [0] * m
        dp[0] = triangle[0][0]
        for i in range(1, m):
            dp[i] = dp[i-1] + triangle[i][i] #处理右边界点,即每一行最右点
            for j in range(i-1, 0, -1):
                dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
            dp[0] += triangle[i][0]     #处理左边界点
        return min(dp)


s = Solution()
x = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(s.minimumTotal(x))
