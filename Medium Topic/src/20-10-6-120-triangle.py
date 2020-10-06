#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/5 23:35
# @Author:JiahangGu
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        动态规划模板题。设dp[i][j]表示到达i,j位置的最小路径和，
        从上到下：dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]，其中要对j的范围做特判，
        因为上行元素个数要少1个。最终答案是min(dp[n-1])
        从下到上：dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]，其中要对j范围做特判。最终答案是dp[0][0]
        然后发现在每一行计算时，只需要利用到前一行的信息，前两行及以外的就不再需要，所以可以将空间复杂度由O(N2)进一步缩减到O(N)，
        并设dp[i]存储的是前一行中i下标位置的最小和。
        从上到下时，dp[i] = min(dp[i-1], dp[i]) + triangle[k][i]，更新i时需要用到i-1的值，所以应该是从右向左更新的顺序，
        否则dp[i-1]的含义就不是上一行，而是当前行。
        不需要额外空间的解法，则可以直接在原始三角矩阵中修改最小路径和。
        :param triangle:
        :return:
        """
        m = len(triangle)
        dp = [1e12] * m
        dp[0] = triangle[0][0]
        for i in range(1, m):
            for j in range(i, -1, -1):
                if j == 0:
                    dp[j] = dp[j] + triangle[i][j]
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + triangle[i][j]
        return min(dp)


s = Solution()
x = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(s.minimumTotal(x))
