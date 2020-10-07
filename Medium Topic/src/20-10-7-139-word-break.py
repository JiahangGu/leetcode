#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/7 18:25
# @Author:JiahangGu
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        暴力做法，回溯：对于剩余的字符串，从长度1开始遍历，如果单词在给定列表里，则剩余字符串继续搜索。
        上述做法会存在重复子问题，例如最后一个单词可能对于不同的路径都要搜索一次。可以使用记忆化搜索来优化，
        使用一个flag数组做记忆化，flag[i]表示从i开始的字符串能否拆分，剩余字符串到i位置时如果flag[i]==True则直接返回。
        :param s:
        :param wordDict:
        :return:
        """
        # def dfs(pos):
        #     if pos >= n:
        #         return True
        #     if pos in flag:
        #         return flag[pos]
        #     for i in range(pos, n):
        #         if s[pos:i+1] in words and dfs(i + 1):
        #             flag[pos] = True
        #             return True
        #     flag[pos] = False
        #     return False
        #
        # n = len(s)
        # flag = dict()
        # words = set()
        # for word in wordDict:
        #     words.add(word)
        # return dfs(0)
        """
        在记忆化搜索基础上进一步使用动态规划的方法做。设dp[i]表示以i结尾的字符串是否可以拆分，则dp[n-1]为答案，初始化为False。
        状态转移方程dp[i] = s[j:i] in wordDict and dp[j]，表示[j,i]表示的字符串在单词字典存在，并且以j结尾的字符串可以拆分，
        则以i结尾的字符串也可以拆分。
        """
        n = len(s)
        dp = [False] * n
        words = set()
        for word in wordDict:
            words.add(word)
        for i in range(n):
            for j in range(i + 1):
                if s[j:i+1] in words and (j == 0 or dp[j - 1]):
                    dp[i] = True
                    break
        return dp[n-1]


s = Solution()
ss = "leetcode"
wordDict = ["leet", "code"]
print(s.wordBreak(ss, wordDict))
