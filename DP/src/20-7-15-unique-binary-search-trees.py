#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/15 10:04
# @Author:JiahangGu


class Solution:
    def numTrees(self, n: int) -> int:
        '''
        二叉搜索树的特点是根节点大于左子树所有节点小于右子数所有节点，所以
        一旦确定根节点值后左子树右子数数字也确定，例如根节点为5，则左子树只
        能是1234，右子树为6-n。而左子树又可以进一步划分为以1，2，3，4为根节
        点的子树，即子树是数字序列的特定排列。
        定义状态dp[n]表示1-n能组成的二叉搜索树的种类，则可以将该二叉树划分为
        左子树i个节点，右子树n-i-1个节点，总方案个数为左子树方案数乘右子树方
        案数。循环过程会包含两次计算，可在n//2处停止循环。
        初始化：dp[0]=1，空树也是一种方案
        解状态：dp[n]
        状态转移方程：dp[i]=sum(dp[j] + dp[i-j-1]) 0<j<i
        :param n:
        :return:
        '''
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            left = 0
            while left < i // 2:
                dp[i] += 2 * dp[left] * dp[i-left-1]
                left += 1
            if (i+1) % 2 == 0:
                dp[i] += dp[i // 2] * dp[i // 2]
        return dp[n]


s = Solution()
print(s.numTrees(3))
