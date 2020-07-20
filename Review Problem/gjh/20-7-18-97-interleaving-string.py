#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/18 17:15
# @Author:JiahangGu


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        可以用深搜来做，假设ijk分别表示s1,s2,s3的当前遍历位置
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True
        if s1[i] == s3[k] and s2[j] == s3[k]:
            return dfs(i+1, j, k+1) or dfs(i, j+1, k+1)
        elif s1[i] == s3[k]:
            return dfs(i+1, j, k+1)
        elif s2[j] == s3[k]:
            return dfs(i, j+1, k+1)
        return False
        解法超时，因为第二个if里面左右两个深搜存在重复子状态，
        可以使用记忆化搜索进行优化，首先s1s2的位置就决定了s3
        的位置，因为长度一定相等，所以不需要考虑k，只要记录ij
        的值就可以知道s1s2遍历的位置，这个点是之前一直没有想
        到的，所以记忆化记录vis[i][j]表示s1[i]、s2[j]是否访问
        过，如果访问过就直接返回。
        :param s1:
        :param s2:
        :param s3:
        :return:
        '''
        # vis = [[None] * len(s3) for _ in range(len(s3))]
        #
        # def dfs(i, j, k):
        #     if k == len(s3):
        #         return True
        #     if vis[i][j] is not None:
        #         return vis[i][j]
        #     flag = False
        #     if i < len(s1) and s1[i] == s3[k]:
        #         flag = dfs(i + 1, j, k + 1)
        #     if j < len(s2) and s2[j] == s3[k]:
        #         flag = flag or dfs(i, j + 1, k + 1)
        #     vis[i][j] = flag
        #     return vis[i][j]
        #
        # if len(s1) + len(s2) != len(s3):
        #     return False
        # return dfs(0, 0, 0)
        '''
        dp方法，类似于记忆化搜索，通过记录s1s2的位置就可以达到确定s3位置的目的
        定义状态dp[i][j]表示s1[i]s2[j]是否能交错组成s3[i+j]的结果，
        则初始状态dp[0][0]=True
        解状态dp[m][n]
        状态转移方程：dp[i][j]=(dp[i-1][j] if s1[i]==s3[k]) or (dp[i][j-1] if s2[j]==s3[k])
        '''
        # if len(s1) + len(s2) != len(s3):
        #     return False
        # dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]
        # dp[0][0] = True
        # for i in range(len(s1)+1):
        #     for j in range(len(s2)+1):
        #         k = i + j - 1
        #         # 判断大于0是因为字符串从1开始，等于0时是非法值
        #         if i > 0:
        #             dp[i][j] = dp[i][j] or (dp[i-1][j] and s1[i-1] == s3[k])
        #         if j > 0:
        #             dp[i][j] = dp[i][j] or (dp[i][j-1] and s2[j-1] == s3[k])
        # return dp[len(s1)][len(s2)]
        '''
        空间优化，可以看到状态ij只和前一个有关，即可以使用一维数组来记录之前状态，
        当前索引左边是更新过的之前的状态，右边是待更新的当前状态。
        '''
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [False]*(len(s2)+1)
        dp[0] = True
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                k = i + j - 1
                # 判断大于0是因为字符串从1开始，等于0时是非法状态
                if i > 0:
                    dp[j] = dp[j] and s1[i-1] == s3[k]
                if j > 0:
                    dp[j] = dp[j] or (dp[j-1] and s2[j-1] == s3[k])
        return dp[len(s2)]


s = Solution()
s1 = "a"
s2 = ""
s3 = "c"
print(s.isInterleave(s1, s2, s3))
