#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/6 15:20
# @Author:JiahangGu
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        回溯算法，对当前字符串按照长度[1,n]做划分，如果当前字符串前k位字符串是回文串，则记录下该字符串，并进入
        深层递归。需要一个辅助函数判断前k位字符串是否是回文。
        对于[i,j]来说，判断是否回文在递归过程中可能需要调用多次，可以先使用动态规划方法存储各位置是否是回文串，
        在需要查询时只需要O(1)时间，但是要多用O(n2)空间
        :param s:
        :return:
        """
        def dfs(string, path, pos):
            if not string:
                ans.append(path[:])
                return
            for i in range(len(string)):
                if dp[pos][pos + i]:
                    dfs(string[i+1:], path + [string[:i+1]], pos + i + 1)

        ans = []
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            j = 1
            while i - j >= 0 and i + j < n:
                dp[i - j][i + j] = dp[i - j + 1][i + j - 1] and s[i - j] == s[i + j]
                j += 1
            j = 0
            while i - j >= 0 and i + j + 1 < n:
                dp[i - j][i + j + 1] = dp[i - j + 1][i + j] and s[i - j] == s[i + j + 1]
                j += 1
        # print(dp)
        dfs(s, [], 0)
        return ans


s = Solution()
print(s.partition("aabb"))
