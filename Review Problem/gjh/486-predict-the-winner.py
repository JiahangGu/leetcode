#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/1 17:13
# @Author:JiahangGu
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """
        递归方法：两个玩家，可以求出先手和后手总分的差值，如果差值大于0则先手赢，否则后手赢。这样在一个玩家选取之后，
        加上下一次分值的负数来表示差值。每个玩家可以选择第一个或最后一个，就形成了两个子节点，通过计算两个节点并选择
        最大值可以优先保证先手获胜。
        递归过程中需要注意，如果当前是对手回合，应该返回对手的最大分数，但由于对手回合得分是负数，需要乘-1求最大值之
        后再乘-1变回原值，统一的话就使用flag标志当前回合是我（1）还是对手（-1）
        时间复杂度对于每个点都有两种可能性，共n个点，所以是O(2^n)，但n很小<=20所以可以通过。
        :param nums:
        :return:
        """
        # def dfs(start, end, flag):
        #     if start == end:
        #         return nums[start] * flag
        #     start_score = nums[start] * flag + dfs(start+1, end, -flag)
        #     end_score = nums[end] * flag + dfs(start, end-1, -flag)
        #     return max(start_score * flag, end_score * flag) * flag
        # return dfs(0, len(nums)-1, 1) >= 0
        """
        上述递归解法存在大量的重复子状态的问题，比如要求[2,4]所能得到的最大值，在拿走1时需要求一次，在拿走5时还要
        再求一次，导致了重复状态。可以使用记忆化方法，存储[2,4]的值在下次求解时直接使用。
        由于递归时自顶向下进行，在用dp时就需要逆向的自底向上，假设dp[i][j]表示在还剩[i,j]的数组时所能得到的最大值，
        则当前状态dp[i][j]对应的情况是拿走i或拿走j所能得到的最大值，而拿走i对应得到的分数为nums[i]-dp[i+1][j]，
        拿走j对应得到的分数为nums[j]-dp[i][j-1]，取最大值。
        且dp是逐行更新的，所以可以使用一维数组表示，即数组是从右下角向左上角更新，所以当前行的第j位其实是dp[i][j]，且
        dp[i][j-1]是已经求出来的，所以一维数组表示即可。
        """
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            dp[i] = nums[i]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
        return dp[n-1] >= 0


s = Solution()
print(s.PredictTheWinner([1, 5, 233, 2]))
